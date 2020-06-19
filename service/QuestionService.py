from app.database.model import User,Question
from app.database import db
from service import UserService

def add_question(title,context,user):
    user = UserService.get_user(user)
    q = Question(title,context)
    user.question.append(q)
    db.session.add(q)
    db.session.commit()

def list(page_index=0,page_size=0):
    questions = Question.query.all()
    return questions