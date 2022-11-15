from flask import Blueprint, url_for, render_template, session
from flask_login import current_user, logout_user
from werkzeug.utils import redirect

from flask_ABTest.controls.session_mgmt import BlogSession
from flask_ABTest.controls.user_mgmt import User

bp = Blueprint('blog', __name__, url_prefix='/')


@bp.route('/')
def main():
    if current_user.is_authenticated:
        webpage_name = BlogSession.get_blog_page(current_user.blog_id)
        BlogSession.save_session_info(session['client_id'], current_user.email, webpage_name)
        return render_template(webpage_name, email=current_user.email)
    else:
        webpage_name = BlogSession.get_blog_page()
        BlogSession.save_session_info(session['client_id'], 'anonymous', webpage_name)
        return render_template(webpage_name)


@bp.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.main'))
