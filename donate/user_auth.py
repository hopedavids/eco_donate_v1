from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from .instances import db
from sqlalchemy.exc import IntegrityError
import re


user_auth = Blueprint('user_auth', __name__)



@user_auth.route('/account/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = request.form.get('remember', False)
        
        user = User.query.filter_by(username=username).first()

        if not username or not password:
            flash('Enter a valid username and password')
            return redirect(url_for('user_auth.signin'))

        if user and not check_password_hash(user.password, password):
            flash("Invalid username or password")
            return redirect(url_for('user_auth.signin'))

        elif not user:    
            flash("Enter a valid username or password")
            return redirect(url_for('user_auth.signin'))

        login_user(user, remember=remember)
        user = current_user
        flash("Login successful, welcome back")
        return redirect(url_for('main.index'))
        
    return render_template('backend/accounts/signin.html')


@user_auth.route('/account/register', methods=['GET', 'POST'])
def register():
    try:
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            confirm_password = request.form['confirm password']

            user = User.query.filter_by(email=email).first()
            
            if not username or not email or not password:
                flash('Kindly fill all fields!')
                return redirect(url_for('user_auth.register'))
            
            if username.isupper() or email.isupper():
                flash('Email and Username must be lowercase!')
                return redirect(url_for('user_auth.register'))

            if user:
                flash('username or email taken')
                return redirect(url_for('user_auth.register'))

            if password:
                if password != confirm_password:
                    flash('Passwords do not match', 'error')
                    return redirect(url_for('user_auth.register'))

            
                minimum_length = 8

                if len(password) < minimum_length:
                    flash('Password should be at least {} characters long'.format(minimum_length), 'error')
                    return redirect(url_for('user_auth.register'))

                if not any(char.isalpha() for char in password) or not any(char.isdigit() for char in password):
                    flash('Password should contain alphanumeric', 'error')
                    return redirect(url_for('user_auth.register'))
        
            new_user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            # flash('Account created, please signin')
            return redirect(url_for('user_auth.signin'))
        
        return render_template('backend/accounts/register.html')

    except IntegrityError or UnboundLocalError or TypeError:
        flash('invalid username or password')
        return
    


@user_auth.route('/account/signout')
@login_required
def signout():
    """signout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('user_auth.signin'))
