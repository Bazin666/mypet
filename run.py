from app import create_app
from controller import index
if __name__ == '__main__':
    app = create_app()
    app.run()

