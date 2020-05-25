from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class User(db.Model):
    __tablename__ = 'm_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    question = db.relationship('Question', backref=db.backref('user'))

    def __init__(self, name, password, email):
        self.username = name
        self.email = email
        self.password = password

    def __reduce__(self):
        return '<User %r>' % self.name


class Question(db.Model):
    __tablename__ = 'm_question'
    id = db.Column(db.Integer, primary_key=True)
    question_title = db.Column(db.String(50), nullable=False)
    question_context = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('m_user.id'))
    def __init__(self, question_title, question_context):
        self.question_title = question_title
        self.question_context = question_context