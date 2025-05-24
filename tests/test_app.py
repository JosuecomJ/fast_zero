import re
from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo!'}


def test_root_html_deve_retornar_ok_e_ola_mundo_html():
    client = TestClient(app)

    response = client.get('/ola-mundo-html')

    assert response.status_code == HTTPStatus.OK
    assert response.headers['content-type'] == 'text/html; charset=utf-8'
    assert re.search(r'<h1>Olá mundo!</h1>', response.text)
    assert re.search(r'<title>Olá Mundo</title>', response.text)
