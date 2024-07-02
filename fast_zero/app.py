from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message
app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World', 'batata': 'frita'}

@app.get('/potato', status_code=HTTPStatus.OK, response_model=Message)
def read_potato():
    return {'message': 'batata frita'}