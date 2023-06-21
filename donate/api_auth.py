from flask import Blueprint, request, jsonify
from flask_login import current_user
from flask_jwt_extended import create_access_token, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash
from .instances import csrf, jwt
from datetime import datetime, timedelta
from .models import User


api_auth = Blueprint('api_auth', __name__, url_prefix='/v1/auth')


@api_auth.route('/login', methods=['POST'])
@csrf.exempt
def login():
    username = request.json['username']
    password = request.json['password']

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({
            "data": "null",
            "message": "Username or Password Incorrect",
            "status": "api-error"
        }),401
    
    access_token = create_access_token(identity=username)
    return jsonify({
        "username": username,
        "access_token": access_token
        })
