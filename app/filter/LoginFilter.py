from flask import request, g, jsonify
from app.database.Redis import redis_cli
from utils import JWTUtils
r = redis_cli
import functools
def login_require(route_func):
    @functools.wraps(route_func)
    def vertify(*args,**kwargs):
        try:
            #获取token
            token = request.headers['Authorization']
        except Exception:
            # 没接收的到token,给前端抛出错误
            return jsonify({'code':10000, 'msg':'无token'})

        current_user = request.form['user']

        raw_token = r.get(token)
        JWTUtils.vertify(raw_token,current_user)


