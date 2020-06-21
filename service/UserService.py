from app.database.model import User, Question
from app.database import db
from utils import MiniappUtils
import hashlib


def regist_user(username, password, email='', wx_openid=''):
    try:
        user = get_user(username=username) or None
        if user is None:
            user = User(username, password, email, wx_openid)
            db.session.add(user)
            db.session.commit()
            return user
        else:
            return user
    except:
        return None


def login_user(username: str, password: str):
    try:
        password_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()
        user = get_user(username, password_md5)
        return user
    except Exception:
        return None


def get_user(username: str=None, passowrd: str = None, openid: str = None,userId =None):
    wrapper = {}
    if username:
        wrapper.update({'username': username})
    if (passowrd):
        wrapper.update({'password': passowrd})
    if openid:
        wrapper.update({'wx_openid': openid})
    if userId:
        wrapper.update({'id':userId})
    # user = User.query.filter_by(username = username,password = passowrd,wx_openid = openid).first()
    user = User.query.filter_by(**wrapper).first()
    return user


def wxlogin(wx_userkey: dict, userinfo: dict):
    openid = wx_userkey.get('openid')
    hash_openid = hashlib.md5(str(openid).encode()).hexdigest()
    username = userinfo['userInfo']['nickName'] + '_' + hash_openid[8:-8]
    # userinfo = MiniappUtils.decrypt(encryptedData=)
    try:
        user = get_user(openid=openid)
        if user is not None:
            return user
        else:
            user = regist_user(username=username, password=hash_openid, wx_openid=openid)
            return user
    except:
        try:
            user = regist_user(username=username, password=hash_openid, wx_openid=openid)
            return user
        except:
            return None
