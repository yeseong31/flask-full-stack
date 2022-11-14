import datetime

from flask import Blueprint, url_for, render_template, make_response, jsonify, request
from flask_login import login_user
from werkzeug.utils import redirect

from flask_ABTest.controls.user_mgmt import User

bp = Blueprint('email', __name__, url_prefix='/email')


@bp.route('/subscribe', methods=('GET', 'POST'))
def subscribe():
    if request.method == 'GET':
        print(f'subscribe: {request.args.get("email")}')
        return redirect(url_for('blog.main'))
    elif request.method == 'POST':
        # print(f'subscribe: {request.get_json()}')  # content-type이 application/json인 경우
        print(f'subscribe: {request.form.get("email")}')  # content-type이 form 관련 형태인 경우

        user = User.create(request.form.get('email'), 'A')

        # https://docs.python.org/3/library/datetime.html#timedelta-objects
        login_user(user, remember=True, duration=datetime.timedelta(days=365))  # Remenber Me 활성화

        return redirect(url_for('blog.main'))
