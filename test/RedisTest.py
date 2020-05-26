import redis

r = redis.StrictRedis(host='localhost',port=6379,decode_responses=True)
r.set('t1.t2.t3','asd')

print(r.get('t1.t2.t30'))