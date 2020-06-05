import json

from app import Config
from app.database.Redis import redis_cli
from controller import index
from flask import request, jsonify
from service import UserService, TokenService
import hashlib
import requests as req

r = redis_cli


@index.route('/')
def index_():
    return 'hello'


@index.route('/login', methods=['POST'])
def login():
    form = request.form
    if form['username'] and form['password']:
        username = form['username']
        password = form['password']
        if UserService.login_user(username, password) is not None:
            token = TokenService.createToken(username = username)
            return jsonify({'token': token, 'user': username})
    return jsonify({'error': "登陆失败"})


@index.route('/regist', methods=['POST'])
def reg():
    form = request.form
    if form['username'] and form['password']:
        username = form['username']
        password_md5 = hashlib.md5(form['password'].encode('utf-8')).hexdigest()
        UserService.regist_user(username, password_md5)
    return 'true'


@index.route('/wx_login', methods=['POST'])
def wx_login():
    form = request.form
    userinfo = json.loads(form.get("userinfo", ""))
    js_code = form.get("code")
    appid = Config.WX_APPID
    appsecret = Config.WX_APPSECRET
    url = "https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code".format(
        appid, appsecret, js_code)
    user_key = req.get(url).json()
    user = UserService.wxlogin(user_key, userinfo)
    if user is not None:
        token = TokenService.createToken(username=user.username)
        return jsonify({'token': token, 'user': user.username})
    return jsonify({'error': "登陆失败"})
