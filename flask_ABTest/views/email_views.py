from flask import Blueprint, url_for, render_template, make_response, jsonify, request
from werkzeug.utils import redirect

bp = Blueprint('email', __name__, url_prefix='/email')


@bp.route('/subscribe', methods=('GET', 'POST'))
def subscribe():
    if request.method == 'GET':
        print(f'subscribe: {request.args.get("email")}')
        return redirect(url_for('blog.test'))
    elif request.method == 'POST':
        # print(f'subscribe: {request.get_json()}')  # content-type이 application/json인 경우
        print(f'subscribe: {request.form.get("email")}')  # content-type이 form 관련 형태인 경우
        return redirect(url_for('blog.test'))
