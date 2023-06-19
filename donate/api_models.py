from flask_restx import fields
from .instances import api


user_model = api.model(
    "User", {
        "id": fields.Integer,
        "username": fields.String
    }
)

user_input_model = api.model(
    "User", {
        "username": fields.String,
        "email": fields.String,
        "password": fields.String
    }
)