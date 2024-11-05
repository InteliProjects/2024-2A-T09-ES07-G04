import pytest
from app import create_app
from unittest.mock import patch

@pytest.fixture
def app():
    """Configura uma instância do Flask para testes."""
    app = createApp('testing')
    with app.app_context():
        yield app

@pytest.fixture
def client(app):
    """Configura um cliente de teste."""
    return app.test_client()

def test_scraping_bacen_missing_url(client):
    """Teste para a rota scraping Bacen com campo URL ausente."""
    response = client.post('/scraping/bacen', json={})
    assert response.status_code == 400
    assert response.get_json()['error'] == "Missing field: 'url'"

@patch('app.service.ScrapingService.scraping_bacen')
def test_scraping_bacen_success(scraping_bacen_mock, client):
    """Teste para a rota scraping Bacen com sucesso."""
    # Simulando os dados de scraping retornados pelo serviço
    scraping_bacen_mock.return_value = {
        'title': 'Banco Central do Brasil',
        'content': 'Conteúdo extraído do site'
    }

    data = {
        'url': 'https://www.bcb.gov.br'
    }

    response = client.post('/scraping/bacen', json=data)
    
    assert response.status_code == 201
    assert response.get_json()['title'] == 'Banco Central do Brasil'
    assert response.get_json()['content'] == 'Conteúdo extraído do site'

@patch('app.service.ScrapingService.scraping_bacen')
def test_scraping_bacen_server_error(scraping_bacen_mock, client):
    """Teste para a rota scraping Bacen com erro no servidor."""
    # Simulando uma exceção no serviço de scraping
    scraping_bacen_mock.side_effect = Exception('Erro inesperado no scraping')

    data = {
        'url': 'https://www.bcb.gov.br'
    }

    response = client.post('/scraping/bacen', json=data)
    
    assert response.status_code == 500
    assert 'Erro inesperado no scraping' in response.get_json()['error']
