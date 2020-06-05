from flask import request, jsonify

from app.filter import login_require
from controller import question
from service import QuestionService


@question.route('/question/add',methods=['POST'])
@login_require
def add():
    try:
        title = request.form['question_title']
        context = request.form['question_context']
        user = request.headers.get('User')
    except Exception:
        return jsonify({'code': '0000', 'msg': '请输入正确的标题或内容'})
    try:
        QuestionService.add_question(title, context,user)
    except Exception:
        return jsonify({'code': '123123', 'msg': '增加失败，请重新提交'})
    return jsonify({'code': '123456', 'msg': 'success'})
