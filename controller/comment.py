from flask import request, jsonify

from app.filter import login_require
from controller import comment
from service import CommentService

from app.filter import validator, Rules


@comment.route('/comment/add', methods=['POST'])
@login_require
@validator(Rules.range('comment_context',low=1,up=200))
def add():
    try:
        context = request.form['comment_context']
        qid = request.form.get('qid','')
        CommentService.add(qid = qid,comment_context = context)
        return jsonify({'code': '10000', 'msg': '成功'})
    except Exception:
        return jsonify({'code': '0000', 'msg': '请输入正确的内容'})