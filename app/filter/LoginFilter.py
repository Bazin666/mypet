from flask import request, g, jsonify

from app import Config
from app.database.Redis import redis_cli
from utils import JWTUtils

r = redis_cli
import functools


def login_require(route_func):
    @functools.wraps(route_func)
    def login_vertify(*args, **kwargs):
        try:
            # 获取token以及当前用户
            current_user = request.headers.get('User')
            token = request.headers.get('AUTHORIZATION')
        except Exception as e:
            # 没接收的到token或用户,给前端抛出错误
            print(e)
            return jsonify({'code': 10000, 'msg': '登陆信息错误，请重新登陆'})
        try:
            #从redis中取出缓存token，并且解析token保存的用户信息
            curr = Config.REDIS_TOKEN_PRE+current_user
            r_token = r.get(Config.REDIS_TOKEN_PRE+current_user)
            r_user = JWTUtils.get_data(r_token).get('user')
        except Exception as e:
            #redis无此token
            print(e)
            return jsonify({'code': 10000, 'msg': '登陆信息错误,请重新登陆'})
        if(r_user == current_user and r_token == token):
            return route_func()
        else:
            return jsonify({'code': 10000, 'msg': '登陆信息错误,请重新登陆'})
    return login_vertify

