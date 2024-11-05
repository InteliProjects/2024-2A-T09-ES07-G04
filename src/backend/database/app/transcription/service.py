import os
from flask import jsonify, request
import requests
from requests.auth import HTTPBasicAuth
from .model import db, Transcription
from werkzeug.utils import secure_filename

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

IMB_SPEECH_TO_TEXT_URL = os.getenv('IMB_SPEECH_TO_TEXT_URL')
IMB_SPEECH_TO_TEXT_USERNAME = os.getenv('IMB_SPEECH_TO_TEXT_USERNAME')
IMB_SPEECH_TO_TEXT_PASSWORD = os.getenv('IMB_SPEECH_TO_TEXT_PASSWORD')

class AudioService:
    def send(self, request):
        print('oiii transcribe')
        self.validateAudio()

        # Get audio
        audio_file = request.files['audio']
        filename = secure_filename(audio_file.filename)

        # Verify if the file exceeds the maximum size
        audio_file.seek(0, 2)  
        file_size = audio_file.tell()
        audio_file.seek(0)

        if file_size > MAX_FILE_SIZE:
            return jsonify({"error": "File too large", "message": "O arquivo excede o limite de 5 MB."}), 413

        # Set Content-Type based on file extension
        if audio_file.filename.endswith('.webm'):
            content_type = 'audio/webm'
        else:
            content_type = 'audio/l16; rate=16000'

        # Send POST request with the file and authentication
        response = requests.post(
            IMB_SPEECH_TO_TEXT_URL,
            headers={
                "Content-Type": content_type
            },
            data=audio_file,
            auth=HTTPBasicAuth(IMB_SPEECH_TO_TEXT_USERNAME, IMB_SPEECH_TO_TEXT_PASSWORD)
        )

        if response.status_code == 200:
            transcription_data = response.json()
            transcription_text = transcription_data.get('results')[0]['alternatives'][0]['transcript']

            # Salve a transcrição no banco de dados
            transcription = Transcription(
                audio_name=filename,
                transcription_text=transcription_text
            )
            db.session.add(transcription)
            db.session.commit()

            

            return jsonify(transcription_data)
        else:
            return jsonify({"error": "Error uploading file", "status_code": response.status_code, "message": response.text}), response.status_code

    def validateAudio(self):
        if 'audio' not in request.files:
            return jsonify({"error": "No audio file sent"}), 400
