from utils import JWTUtils
import redis
a1 = {
    'username': 'aa',
    'password': 'bb'
}

jwt = JWTUtils.JWTBuilder().set_claims(a1).build_jwt_token()
print(jwt)

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsInR5cGUiOiJKV1QifQ.eyJpYXQiOjE1OTA0NjA2NDcuOTY1NzYwNSwiZXhwIjoxNTkwNjMzNDQ3Ljk2NTc2MDUsInVzZXJuYW1lIjoiYWEiLCJwYXNzd29yZCI6ImJiIn0.jmkWA7B-XvojPQX1aLgAxZ0yL3DN3iHwgLz92jWgRfE'
t1 = JWTUtils.vertify(token)
print(t1)