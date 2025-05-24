from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI(
    title='API Fast do Zero',
    description='API Fast do Zero',
    version='0.0.1',
    docs_url='/docs',
    redoc_url='/redoc',
)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!'}


@app.get(
    '/ola-mundo-html',
    status_code=HTTPStatus.OK,
    response_class=HTMLResponse,
)
def read_root_html():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Olá Mundo</title>
        </head>
        <body>
            <h1>Olá mundo!</h1>
        </body>
    </html>
    """
