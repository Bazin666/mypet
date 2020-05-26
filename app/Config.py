DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'mypet'
PASSWORD = 'mypet'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'mypet'
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                            DATABASE)

JWT_HEADER_ALG = 'HS256'
JWT_HEADER_TYP = 'JWT'
JWT_KEY = 'www.mypet.com'
JWT_EXPIRE_TIME = 60 * 60 * 24 * 2  #time.time()返回时间戳是秒单位，默认过期时间两天

REDIS_URL = 'localhost'
REDIS_PORT = '6379'
REDIS_PASSWORD = None
