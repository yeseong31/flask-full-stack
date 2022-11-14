from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/test')
def test():
    return render_template('base.html')
