import redis
import app.Config as config
redis_cli = redis.StrictRedis(host=config.REDIS_URL,port=config.REDIS_PORT,password=config.REDIS_PASSWORD,decode_responses=True)
