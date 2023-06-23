from flask import Blueprint, render_template
from flask_login import login_required, current_user


main = Blueprint('main', __name__)

@main.route('/profile')
@login_required
def index():

    user = current_user.username
    return render_template('backend/index.html', user=user)


@main.route('/donations')
@login_required
def donate():
    return render_template('backend/pages/donate.html')


@main.route('/thank-you')
@login_required
def after_payment():
    return render_template('backend/pages/thank-you.html')