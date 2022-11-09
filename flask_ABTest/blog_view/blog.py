import datetime

from flask import Blueprint, session, render_template, request, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user

from flask_ABTest.blog_control.session_mgmt import BlogSession
from flask_ABTest.blog_control.user_mgmt import User

blog_abtest = Blueprint('blog', __name__)

# 복잡한 소스 파일에서는 코드를 분리하여 MVC 패턴을 정확하게 따라서,
# 리턴할 view 데이터 생성을 위한 함수들을 control 에 넣을 수 있음
# 간단한 코드일 경우에는, 기능별로 모아 놓는 것이 여러 파일을 왔디 갔다 하지 않아서, 더 유용함
# MVC 패턴은 케이스에 따라 사용하는 것이 합리적임


@blog_abtest.route('/auth')
@login_required
def auth_test():
    return 'auth'


@blog_abtest.route('/set_email')
def set_email():
    user_email = request.args.get('user_email')
    blog_id = request.args.get('blog_id')
    user = User.create(user_email, blog_id)
    login_user(user, remember=True, duration=datetime.timedelta(days=365))
    # login_user(user)
    # return render_template(get_blog_page(blog_id), user_email=user_email)
    # return redirect(url_for('blog.blog', blog_id=blog_id, user_email=user_email))
    return redirect(url_for('blog.blog'))


@blog_abtest.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.blog'))


@blog_abtest.route('/blog1')
def blog():
    # user_email = request.args.get('user_email')
    # blog_id = request.args.get('blog_id')
    # 로그인을 했다면
    if current_user.is_authenticated:
        webpage_name = BlogSession.get_blog_page(current_user.blog_id)
        BlogSession.save_session_info(session['client_id'], current_user.user_email, webpage_name)
        return render_template(webpage_name, user_email=current_user.user_email)
    # 로그인을 하지 않았다면
    else:
        webpage_name = BlogSession.get_blog_page()
        BlogSession.save_session_info(session['client_id'], 'anonymous', webpage_name)
        return render_template(webpage_name)
