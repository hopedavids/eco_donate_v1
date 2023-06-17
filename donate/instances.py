from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_login import LoginManager


"""This is where initialization of the app and db takes place."""

api = Api()

db = SQLAlchemy()

jwt = JWTManager()

login_manager = LoginManager()

login_manager.login_view = 'user_auth.signin'