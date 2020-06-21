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


@question.route('/questions/all', methods=['GET'])
@login_require
def all():
    q_list = QuestionService.list()
    res = []
    for q in q_list:
        comment = []
        for c in q.comment:
            comment.append(c.comment_context)
        res.append({"title": q.question_title, "context": q.question_context, 'id': q.id,'comments':comment})

    r = jsonify(res)
    return r

@question.route('/questions', methods=['GET'])
@login_require
def all_by_one():
    userid = request.args.get('userid','')
    q_list = QuestionService.list_by_one(username=userid)
    res = []
    for q in q_list:
        res.append({"title": q.question_title, "context": q.question_context, 'id': q.id})
    r = jsonify(res)
    return r

@question.route('/question', methods=['GET'])
@login_require
def get_one():
    qid = request.args.get('qid','')
    question = QuestionService.getOne(qid)
    comments = []
    for c in question.comment:
        comments.append(c.comment_context)



    r = {'qid': question.id,'title':question.question_title,'context':question.question_context,'comments':comments}
    if r:
        r = jsonify(r)
        return r
    return jsonify({})


@question.route('/question/rev', methods=['POST'])
@login_require
@validator(Rules.range('title',1,50),
           Rules.range('context',1,250))
def rev():
    try:
        title = request.form.get('title')
        id = request.form.get('qid')
        context = request.form.get('context')
        issuccess = QuestionService.rev(title=title,context=context,id=id)
        if(issuccess):
            return jsonify({'code':10000,'msg':'修改成功'})
        else:
            return jsonify({'code': 10001, 'msg': '修改失败'})
    except:
        return jsonify({'code': 10001, 'msg': '修改失败'})

@question.route('/question/delete', methods=['POST'])
@login_require
def delete():
    try:
        id = request.form.get('qid')
        issuccess = QuestionService.delete(id=id)
        if(issuccess):
            return jsonify({'code':10000,'msg':'删除成功'})
        else:
            return jsonify({'code': 10001, 'msg': '删除失败'})
    except:
        return jsonify({'code': 10001, 'msg': '删除失败'})