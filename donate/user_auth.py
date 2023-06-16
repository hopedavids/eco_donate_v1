from flask import Blueprint, render_template, redirect, url_for


user_auth = Blueprint('user_auth', __name__)


@user_auth.route('/signin')
def signin():
    return render_template('backend/pages/sign-in.html')


@user_auth.route('/signup')
def signup():
    return render_template('backend/pages/sign-up.html')


@user_auth.route('/signout')
def signout():
    return redirect(url_for('main.index'))