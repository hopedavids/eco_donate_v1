from flask_restx import fields
from .instances import api


wallet_model = api.model(
    "Wallet", {
        "wallet_id": fields.String,
        "user_id": fields.Integer,
        "current_balance": fields.Float,
        "previous_balance": fields.Float,
        "created_at": fields.DateTime(dt_format='iso8601'),
        "updated_at": fields.DateTime(dt_format='iso8601')
    }
)


user_model = api.model(
    "User", {
        "id": fields.Integer,
        "username": fields.String,
        "email": fields.String,
        "email_confirm": fields.Boolean,
        "created_date": fields.DateTime(dt_format='iso8601'),
        "email_confirm_at": fields.DateTime(dt_format='iso8601')
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



payment_model = api.model(
    "Payment", {
        "payment_id": fields.Integer,
        "wallet_id": fields.String,
        "donation_id": fields.Integer,
        "amount": fields.Float,
        "timestamp": fields.DateTime(dt_format='iso8601')
    }
)