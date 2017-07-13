from flask import request
import jwt
from jwt import DecodeError

from api.settings import Configurations


def generate_token(user):
    token = jwt.encode({
        'id': user.id,
        'username': user.username
    }, Configurations.jwt_key, algorithm=Configurations.jwt_algorithm)

    return token.decode('utf-8')


def check_user():
    token = request.headers.get('Token')

    if token is None:
        return False

    try:
        user = jwt.decode(token, Configurations.jwt_key, algorithms=[Configurations.jwt_algorithm])
        return True
    except DecodeError:
        return False
