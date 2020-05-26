from flask import Flask
from app import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    regist_controller(app)
    from app.database.model import db
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app


def regist_controller(app:Flask):
    from controller import index,question
    app.register_blueprint(index)
    app.register_blueprint(question)