import pytest
from app import create_app, db
from app.models import Regulation

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
    regulation = Regulation(
        regulatorid=1,
        documenttypeid=1,
        documentnumber=1234,
        publicationdate='2024-01-01',
        topic='Saúde Pública',
        organizationid=1,
        status=True,
        documenturl='http://example.com/doc1',
        xmltext='<xml></xml>',
        plaintext='Regulação de exemplo'
    )
    db.session.add(regulation)
    db.session.commit()

def test_get_all_regulations(client, init_database):
    """Teste para a rota GET /regulations."""
    response = client.get('/regulations')
    assert response.status_code == 200
    assert len(response.get_json()) == 1  # Deve retornar uma regulação no banco

def test_get_regulation_by_id(client, init_database):
    """Teste para a rota GET /regulations/<id>."""
    response = client.get('/regulations/1')
    assert response.status_code == 200
    assert response.get_json()['id'] == 1

def test_create_regulation(client):
    """Teste para a rota POST /regulations."""
    new_regulation = {
        "regulatorid": 2,
        "documenttypeid": 1,
        "documentnumber": 5678,
        "publicationdate": "2024-02-01",
        "topic": "Educação",
        "organizationid": 2,
        "status": True,
        "documenturl": "http://example.com/doc2",
        "xmltext": "<xml>novo</xml>",
        "plaintext": "Nova regulação"
    }
    response = client.post('/regulations', json=new_regulation)
    assert response.status_code == 201
    assert response.get_json()['documentnumber'] == 5678

def test_execute_sql_query(client):
    """Teste para a rota POST /regulations/query."""
    query = {"text": "SELECT * FROM regulation"}
    response = client.post('/regulations/query', json=query)
    assert response.status_code == 200
    assert len(response.get_json()) > 0  # Deve retornar pelo menos 1 regulação
