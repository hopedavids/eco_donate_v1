from flask_restx import fields
from .instances import api



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


user_creation_model = api.model(
    "User", {
        "username": fields.String(required=True),
        "email": fields.String(required=True),
        "password": fields.String(required=True),
    }
)




api_auth =  {
        "username": fields.String,
        "email": fields.String,
        'login_date': fields.DateTime(dt_format='iso8601')

    }


wallet_model = api.model(
    "Wallet", {
        "wallet_id": fields.String,
        "user": fields.Nested(user_model),       
        "current_balance": fields.Float,
        "previous_balance": fields.Float,
        "created_at": fields.DateTime(dt_format='iso8601'),
        "updated_at": fields.DateTime(dt_format='iso8601')
    }
)


contact_model = api.model(
    "Contact", {
        "contact_id": fields.Integer,
        "user": fields.Nested(user_model),
        "full_name": fields.String,
        "address": fields.String,
        "country": fields.String,
        "about_me": fields.String
    }
)


donation_model = api.model(
    "Donation", {
        "donation_id": fields.Integer,
        "user": fields.Nested(user_model),
        "amount": fields.Float,
        "tree_spieces": fields.String,
        "number_of_trees": fields.String,
        "region_to_plant": fields.String,
        "description": fields.String,
        "get_certified": fields.Boolean,
        "timestamp": fields.DateTime(dt_format='iso8601')
    }
)

payment_model = api.model(
    "Payment", {
        "payment_id": fields.Integer,
        "wallet_id": fields.String,
        "donation": fields.Nested(donation_model),
        "amount": fields.Float,
        "timestamp": fields.DateTime(dt_format='iso8601')
    }
)