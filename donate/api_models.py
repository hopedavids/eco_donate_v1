from flask_restx import fields
from .instances import api


user_model = api.model(
    "User", {
        "id": fields.Integer,
        "username": fields.String,
        "email": fields.String
    }
)

user_input_model = api.model(
    "User", {
        "username": fields.String,
        "email": fields.String,
        "password": fields.String
    }
)

api_auth =  {
        "username": fields.String,
        "email": fields.String,
        'login_date': fields.DateTime(dt_format='iso8601')

    }

wallet_model = api.model(
    "Wallet", {
        "wallet_id": fields.String
    }
)