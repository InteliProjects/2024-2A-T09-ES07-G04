import pytest
from app import create_app, db
from app.models import Regulator, Organization

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
    """Inicializa o banco de dados com dados de exemplo."""
    regulator = Regulator(
        name='Agência Nacional de Saúde',
        scrapingurl='http://example.com/ans'
    )
    organization = Organization(
        name='Ministério da Saúde'
    )
    db.session.add(regulator)
    db.session.add(organization)
    db.session.commit()

def test_get_all_regulators(client, init_database):
    """Teste para a rota GET /regulators."""
    response = client.get('/regulators')
    assert response.status_code == 200
    assert len(response.get_json()) == 1  # Deve retornar um regulador no banco
    assert response.get_json()[0]['name'] == 'Agência Nacional de Saúde'

def test_get_regulator_by_id(client, init_database):
    """Teste para a rota GET /regulators/<id>."""
    response = client.get('/regulators/1')
    assert response.status_code == 200
    assert response.get_json()['id'] == 1
    assert response.get_json()['name'] == 'Agência Nacional de Saúde'

def test_get_regulator_by_id_not_found(client):
    """Teste para a rota GET /regulators/<id> quando o regulador não existe."""
    response = client.get('/regulators/999')  # ID que não existe
    assert response.status_code == 404
    assert response.get_json()['error'] == 'Regulador não encontrado'

def test_get_all_organizations(client, init_database):
    """Teste para a rota GET /regulators/organization."""
    response = client.get('/regulators/organization')
    assert response.status_code == 200
    assert len(response.get_json()) == 1  # Deve retornar uma organização no banco
    assert response.get_json()[0]['name'] == 'Ministério da Saúde'

def test_get_organization_by_id(client, init_database):
    """Teste para a rota GET /regulators/organization/<id>."""
    response = client.get('/regulators/organization/1')
    assert response.status_code == 200
    assert response.get_json()['id'] == 1
    assert response.get_json()['name'] == 'Ministério da Saúde'

def test_get_organization_by_id_not_found(client):
    """Teste para a rota GET /regulators/organization/<id> quando a organização não existe."""
    response = client.get('/regulators/organization/999')  # ID que não existe
    assert response.status_code == 404
    assert response.get_json()['error'] == 'Organização não encontrada'
