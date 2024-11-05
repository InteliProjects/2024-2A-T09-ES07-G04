import pytest
import requests_mock
import json
from app import create_app, db
from unittest.mock import patch

@pytest.fixture
def app():
    """Configura uma instância do Flask para testes."""
    app = createApp('testing')  # Assumindo que você tem uma configuração de 'testing'
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Configura um cliente de teste."""
    return app.test_client()

def test_pln_model_no_input(client):
    """Teste para a rota PLN com falta de input."""
    response = client.post('/pln/', json={})
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Nenhum texto fornecido'

@patch('app.services.preprocess_text')
def test_pln_model_success(preprocess_text_mock, client):
    """Teste para a rota PLN com input válido."""
    preprocess_text_mock.return_value = 'texto preprocessado'

    mock_model_response = [1]  # Simulando a previsão do modelo
    with patch('app.blueprints.pln.modelo.predict', return_value=mock_model_response):
        response = client.post('/pln/', json={'input': 'Texto de exemplo'})

    assert response.status_code == 200
    assert response.get_json()['resultado'] == 1

def test_webhook_scraping_success(client, requests_mock):
    """Teste para o webhook de scraping com sucesso."""
    webhook_db_url = 'http://127.0.0.1:5000/regulations'
    webhook_response_data = {'status': 'Data enviada para o banco com sucesso'}
    
    # Simulando o retorno do banco de dados
    requests_mock.post(webhook_db_url, json=webhook_response_data)

    # Dados enviados pelo webhook
    test_data = {
        "regulatorid": 201,
        "title": "New Regulation Title",
        "topic": "Financial Services",
        "description": "This is a description of the new regulation regarding financial services.",
        "documenturl": "https://example.com/regulation.pdf",
        "status": True,
        "publicationdate": "2024-09-13T00:00:00Z",
        "tags": [
            {
                "name": "Finance",
                "color": "#434343"
            }
        ]
    }

    response = client.post('/pln/webhook-scraping', json=test_data)
    assert response.status_code == 200
    assert response.get_json()['status'] == 'Data enviada para o banco com sucesso'

def test_webhook_scraping_no_data(client):
    """Teste para o webhook de scraping sem dados JSON."""
    response = client.post('/pln/webhook-scraping', json={})
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Nenhum dado JSON enviado'

def test_rabbitmq_consumer_message_handling(requests_mock):
    """Teste para o consumidor RabbitMQ processar mensagens corretamente."""
    # Simula a resposta do webhook
    webhook_url = 'http://127.0.0.1:5000/pln/webhook-scraping'
    requests_mock.post(webhook_url, json={'status': 'success'}, status_code=200)

    # Simulação da mensagem recebida via RabbitMQ
    body = json.dumps({"input": "test data"}).encode('utf-8')

    with patch('app.blueprints.pln.pika.BlockingConnection'):
        from app.blueprints.pln import start_rabbitmq_consumer
        
        # Simula o comportamento da fila RabbitMQ
        mock_channel = patch('app.blueprints.pln.pika.channel').start()
        mock_channel.basic_consume = patch('app.blueprints.pln.pika.channel.basic_consume').start()

        start_rabbitmq_consumer()

        mock_channel.basic_consume.assert_called_once()

def test_regulation_pln_route(client):
    """Teste para a rota PLN pipeline."""
    test_input = {"input": "Texto de exemplo para PLN"}
    
    # Mock da função pln_query_pipeline
    with patch('app.blueprints.pln.pln_query_pipeline', return_value={"result": "sucesso"}):
        response = client.post('/pln/query', json=test_input)

    assert response.status_code == 200
    assert response.get_json()['result'] == "sucesso"

def test_test_pln_route(client):
    """Teste para verificar a rota de teste."""
    response = client.get('/pln')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "It's works"
