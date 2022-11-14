from flask import Blueprint, url_for, render_template
from flask_login import current_user, logout_user
from werkzeug.utils import redirect

bp = Blueprint('blog', __name__, url_prefix='/')


@bp.route('/')
def main():
    if current_user.is_authenticated:
        return render_template('blog_A.html', email=current_user.email)
    return render_template('blog_A.html')


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('blog.main'))
