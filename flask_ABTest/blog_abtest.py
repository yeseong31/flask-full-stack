from flask import Flask, make_response, jsonify, session, request
from flask_cors import CORS
from flask_login import LoginManager

import config
from flask_ABTest.blog_control.user_mgmt import User
from flask_ABTest.blog_view import blog

from flaskext.markdown import Markdown

HOST_NUM = '0.0.0.0'
PORT_NUM = 5000

# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = os.getenv('OAUTHLIB_INSECURE_TRANSPORT')

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secret_key = config.SECRET_KEY

app.register_blueprint(blog.blog_abtest, url_prefix='/blog')

Markdown(app, extensions=['nl2br', 'fenced_code'])

# User Session Management Setup
login_manager = LoginManager()
login_manager.init_app(app)  # app login_manager 연결
login_manager.session_protection = 'strong'


@login_manager.user_loader
def load_user(user_id):
    """로그인 후 최초 current_user 호출 시 동작 제어"""
    return User.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    """로그인이 되지 않은 사용자의 페이지 접근 제어"""
    return make_response(jsonify(success=False), 401)


@app.before_request
def before_request():
    if 'client_id' not in session:
        session['client_id'] = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)


if __name__ == '__main__':
    app.run(host=HOST_NUM, port=PORT_NUM)
