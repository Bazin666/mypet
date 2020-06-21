from app.database.model import User,Question,Comment
from app.database import db
from service import UserService,QuestionService


def add(qid,comment_context):
    try:
        comment = Comment(comment_context)
        q = QuestionService.getOne(qid)
        userid = q.user_id
        u = UserService.get_user(userId=q.user_id)
        q.comment.append(comment)
        u.comment.append(comment)
        db.session.add(comment)
        db.session.commit()
        return comment
    except:
        return None