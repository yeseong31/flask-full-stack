from flask import Blueprint, url_for, render_template
from flask_login import current_user, logout_user
from werkzeug.utils import redirect

from flask_ABTest.controls.user_mgmt import User

bp = Blueprint('blog', __name__, url_prefix='/')


@bp.route('/')
def main():
    if current_user.is_authenticated:
        return render_template('blog_A.html', email=current_user.email)
    return render_template('blog_A.html')


@bp.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.main'))
