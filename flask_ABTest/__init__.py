import os

from flask import Flask, jsonify, make_response, request, render_template, g
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS

import config

from flask_ABTest.controls.user_mgmt import User


# HTTPS만을 지원하는 기능을 HTTP에서 테스트할 때 필요한 설정
from flask_ABTest.views import email_views

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


# Application Factory
def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(config)
    CORS(app)
    app.secret_key = os.getenv('SECRET_KEY')

    # ----- Blueprint -----
    from .views import blog_views
    app.register_blueprint(blog_views.bp)
    app.register_blueprint(email_views.bp)

    # ----- flask_login -----
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.session_protection = 'strong'

    @login_manager.user_loader
    def user_loader(user_id):
        """로그인 후 최초 current_user 호출 시 동작 제어"""
        return User.get(user_id)

    @login_manager.unauthorized_handler
    def unauthorized():
        """로그인이 되지 않은 사용자의 페이지 접근 제어"""
        return make_response(jsonify(success=False), 401)

    return app
