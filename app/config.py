
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
