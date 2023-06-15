from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_jwt_extended import JWTManager


"""This is where initialization of the app and db takes place."""

api = Api()

db = SQLAlchemy()

jwt = JWTManager()