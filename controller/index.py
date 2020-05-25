from controller import index

@index.route('/')
def index_():
    return 'hello'

@index.route('/login')
def login():
    
    return 'login'