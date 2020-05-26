from app import Config
from app.database.Redis import redis_cli
from controller import index
from flask import request,g
from app.filter.LoginFilter import login_require
from utils import JWTUtils
import hashlib

r = redis_cli

@index.route('/')
def index_():
    return 'hello'


@index.route('/login',methods = ['POST'])
def login():
    user = request.form['username']
    token = JWTUtils.JWTBuilder().set_claims({user:user}).build_jwt_token()
    token_md5 = hashlib.md5(token.encode('utf-8')).hexdigest()
    pre = user+'.'+'JWT_TOKEN'
    if(r.exists(pre)):
        r.delete(pre)
    r.set(pre+'.'+token_md5,token)
    return token_md5