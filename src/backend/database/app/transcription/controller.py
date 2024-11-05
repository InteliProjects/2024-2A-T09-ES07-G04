from .service import AudioService
from flask import Blueprint
from flask import request

audio_blueprint = Blueprint('audio', __name__)
audio_service = AudioService()

@audio_blueprint.route('/transcribe', methods=['POST'])
def send():
    return audio_service.send(request=request)
