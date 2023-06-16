from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/landing_page')
def index():
    return render_template('backend/index.html')