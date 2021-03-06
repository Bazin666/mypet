import time

from Crypto.Cipher import AES
import jwt
from app import Config
from binascii import b2a_hex, a2b_hex, hexlify
from app.database.Redis import redis_cli as r
import hashlib
"""payload 中一些固定参数名称的意义, 同时可以在payload中自定义参数"""
# iss  【issuer】发布者的url地址
# sub 【subject】该JWT所面向的用户，用于处理特定应用，不是常用的字段
# aud 【audience】接受者的url地址
# exp 【expiration】 该jwt销毁的时间；unix时间戳
# nbf  【not before】 该jwt的使用时间不能早于该时间；unix时间戳
# iat   【issued at】 该jwt的发布时间；unix 时间戳
# jti    【JWT ID】 该jwt的唯一ID编号

payload = {
    'iat': None,
    'user': ''
}

"""headers 中一些固定参数名称的意义"""
# jku: 发送JWK的地址；最好用HTTPS来传输
# jwk: 就是之前说的JWK
# kid: jwk的ID编号
# x5u: 指向一组X509公共证书的URL
# x5c: X509证书链
# x5t：X509证书的SHA-1指纹
# x5t#S256: X509证书的SHA-256指纹
# typ: 在原本未加密的JWT的基础上增加了 JOSE 和 JOSE+ JSON。JOSE序列化后文会说及。适用于JOSE标头的对象与此JWT混合的情况。
# crit: 字符串数组，包含声明的名称，用作实现定义的扩展，必须由 this->JWT的解析器处理。不常见。

header = {
    'alg': Config.JWT_HEADER_ALG,
    'type': Config.JWT_HEADER_TYP
}


class JWTBuilder:
    header = header
    payload = payload

    def __init__(self):
        self.payload.update({'iat':time.time()})
        self.set_expire()

    def set_expire(self, expire_time=Config.JWT_EXPIRE_TIME):
        self.payload['exp'] = self.payload['iat'] + expire_time
        return self

    def set_claims(self, claims: dict):
        payload.update(claims)
        return self

    def build_jwt_token(self):
        # 生成token的Byte字节
        token = jwt.encode(
            payload,
            algorithm='HS256',
            headers=header,
            key=Config.JWT_KEY
        )
        # 将token的Byte字节转换为数字+英文+符号
        return token.decode()


def vertify(token: str, user: str):
    try:
        token = decrypt(token)
        data = jwt.decode(token, key=Config.JWT_KEY, algorithms='HS256')
        return True
    except Exception as e:
        print(e)
        return False

def get_data(data):
    return jwt.decode(decrypt(data),key=Config.JWT_KEY,algorithms='HS256')

def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')

def encrypt(text):
    key = add_to_16(Config.JWT_KEY)
    mode  = AES.MODE_CBC
    iv = add_to_16(Config.AES_IV)
    text = add_to_16(text)
    cryptos = AES.new(key,mode,iv)
    cipher_text = cryptos.encrypt(text)
    return b2a_hex(cipher_text).decode()

def decrypt(text):
    key = add_to_16(Config.JWT_KEY)
    mode = AES.MODE_CBC
    iv = add_to_16(Config.AES_IV)
    text = add_to_16(text)
    cryptos = AES.new(key,mode,iv)
    raw_text = cryptos.decrypt(a2b_hex(text))
    return bytes.decode(raw_text).rstrip('\0')