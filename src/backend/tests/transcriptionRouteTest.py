import io
import pytest
from app import create_app, db
from app.models import Transcription
from unittest.mock import patch
import requests_mock

@pytest.fixture
def app():
    """Configura uma instância do Flask para testes."""
    app = createApp('testing')  
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Configura um cliente de teste."""
    return app.test_client()

@pytest.fixture
def init_database(app):
    """Inicializa o banco de dados com uma transcrição de exemplo."""
    transcription = Transcription(
        audio_name='example_audio.wav',
        transcription_text='Texto de exemplo transcrito.'
    )
    db.session.add(transcription)
    db.session.commit()

def test_send_audio_file(client, requests_mock):
    """Teste para enviar um arquivo de áudio e receber a transcrição."""
    
    # Simulando a resposta do IBM Speech to Text API
    transcription_mock_response = {
        "results": [{
            "alternatives": [{
                "transcript": "Esta é uma transcrição de teste."
            }]
        }]
    }

    requests_mock.post('https://mock-imb-speech-to-text-url', json=transcription_mock_response)

    # Simulando o envio de um arquivo de áudio
    data = {
        'audio': (io.BytesIO(b"fake audio data"), 'audio.wav')
    }
    
    response = client.post('/audio/transcribe', data=data, content_type='multipart/form-data')

    assert response.status_code == 200
    assert 'Esta é uma transcrição de teste.' in response.get_json()['results'][0]['alternatives'][0]['transcript']

def test_file_too_large(client):
    """Teste para verificar o comportamento ao enviar um arquivo maior que o limite."""
    
    # Simulando um arquivo maior que 5 MB
    large_file = io.BytesIO(b"a" * (5 * 1024 * 1024 + 1))  # 5 MB + 1 byte
    
    data = {
        'audio': (large_file, 'large_audio.wav')
    }

    response = client.post('/audio/transcribe', data=data, content_type='multipart/form-data')

    assert response.status_code == 413
    assert response.get_json()['error'] == "File too large"

def test_no_audio_file(client):
    """Teste para verificar o comportamento ao não enviar um arquivo de áudio."""
    
    data = {}

    response = client.post('/audio/transcribe', data=data, content_type='multipart/form-data')

    assert response.status_code == 400
    assert response.get_json()['error'] == "No audio file sent"
