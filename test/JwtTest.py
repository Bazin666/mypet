from utils import JWTUtils
import redis
a1 = {
    'username': 'aa',
    'password': 'bb'
}

# jwt = JWTUtils.JWTBuilder().set_claims(a1).build_jwt_token()
# print(jwt)

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsInR5cGUiOiJKV1QifQ.eyJpYXQiOjE1OTA0NjA2NDcuOTY1NzYwNSwiZXhwIjoxNTkwNjMzNDQ3Ljk2NTc2MDUsInVzZXJuYW1lIjoiYWEiLCJwYXNzd29yZCI6ImJiIn0.jmkWA7B-XvojPQX1aLgAxZ0yL3DN3iHwgLz92jWgRfE'

t1 = JWTUtils.encrypt(token)
t2 = t1.decode('utf-8')
r1 = JWTUtils.decrypt('ab306dcb8bfc3813961a36a795a2dcfa9e5bbce65ae0d7fe8c000448dd37be3cd28d16aa579d501dc3df5c4148fbd067cd1c6c2eaf179ebf28a6f51ba0d00b8111b2404a1afc8478846c3bc73447f8e64cd26be79489539e613292f466063231ad258a22f9fe0813abe17dce0169edf52fca90edbf7131be7f7d47683c72a89e07091d655da5bd6160b2e135c2b027db0c5134a45839a33448ec23a3d6a97b3e1866298cbca1e32eca04cb850ef482dfab0691bc9248766f60c45a28b799f5a5b61549b1fb6e52059c011f8aae2cd245d5157d130d2b6dc4bf3a957bdb719324')
print(t2)
print(r1)