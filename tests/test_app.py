from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo!'}


def test_create_user_deve_retornar_user():
    client = TestClient(app)

    response = client.post(
        '/users/',
        json={'username': 'João',
              'email': 'joao@example.com',
              'password': '123'
              }
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'João',
        'email': 'joao@example.com',
        'password': '123'
    }
