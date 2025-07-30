from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message, UserSchema

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


@app.post('/users/', status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    return user
