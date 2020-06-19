from flask import request, jsonify

from app.filter import login_require
from controller import question
from service import QuestionService

from app.filter import validator, Rules


@question.route('/question/add', methods=['POST'])
@login_require
@validator(Rules.range('question_title',1,50),
           Rules.range('question_context',1,250))
def add():
    try:
        title = request.form['question_title']
        context = request.form['question_context']
        user = request.headers.get('User')
    except Exception:
        return jsonify({'code': '0000', 'msg': '请输入正确的标题或内容'})
    try:
        QuestionService.add_question(title, context, user)
    except Exception:
        return jsonify({'code': '123123', 'msg': '增加失败，请重新提交'})
    return jsonify({'code': '123456', 'msg': 'success'})


@question.route('/questions', methods=['GET'])
@login_require
def all():
    q_list = QuestionService.list()
    res = []
    for q in q_list:
        res.append({"title": q.question_title, "context": q.question_context, 'id': q.id})
    r = jsonify(res)
    return r
