from flask import jsonify

from app import Config
from service import UserService
from utils import JWTUtils
from app.database.Redis import redis_cli

r = redis_cli


def createToken(username:str):
    raw_token = JWTUtils.JWTBuilder().set_claims({'user': username}).build_jwt_token()
    token = JWTUtils.encrypt(raw_token)
    try:
        if (r.get(Config.REDIS_TOKEN_PRE + username)) != None or (r.get(Config.REDIS_TOKEN_PRE + username)) != '':
            r.delete(Config.REDIS_TOKEN_PRE + username)
        r.set(Config.REDIS_TOKEN_PRE + username, token)
        return token
    except Exception:
        return None
