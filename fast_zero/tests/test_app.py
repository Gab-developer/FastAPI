from http import HTTPStatus
import pytest
from fastapi.testclient import TestClient
from fast_zero.app import app

@pytest.fixture()
def client():
    client = TestClient(app)

def test_read_root_deve_retornar_ok_e_ola_mundo(client):

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá, Mundo!'}

def test_create_user(client):
    response = client.post('/users/', json={
        'username': 'testeusername',
        'password': 'password',
        'email': 'test@test.com'
        }
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testeusername',
        'email': 'test@test.com',
        'id': 1
    }

