from flask import Blueprint
from werkzeug.security import check_password_hash, generate_password_hash


api_auth = Blueprint('api_auth', __name__, url_prefix=)

