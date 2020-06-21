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

def list_by_one(page_index=0,page_size=0,username=None):
    question = []
    try:
        user = UserService.get_user(username=username)
        q = user.question
        return user.question
    except:
        return []


def getOne(qid):
    try:
        # q = Question.query.filter_by(id=qid).first()
        q = Question.query.get(qid)
        return q
    except:
        return {}


def rev(title,context,id):
    try:
        r = {'question_title':title,'question_context':context}
        q = Question.query.get(id)
        # Question.query.filter_by(id = id).update(r)
        q.question_title = title
        q.question_context = context
        # Question.query.update(q)
        db.session.commit()
        return True
    except:
        return False


def delete(id):
    try :
        Question.query.filter_by(id=id).delete()
        db.session.commit()
        return True
    except:
        return False