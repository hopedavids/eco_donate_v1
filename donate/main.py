from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/landing_page')
@login_required
def index():
    return render_template('backend/index.html')