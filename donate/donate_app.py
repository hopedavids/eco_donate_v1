import os
import psycopg2
from flask import Flask
from dotenv import load_dotenv
from flask_login import LoginManager
from .instances import api, db, jwt
# from flask_jwt_extended import JWTManager
from sqlalchemy.dialects.postgresql import psycopg2
from .resources import auth_ns, user_ns, wallet_ns, pay_ns, trans_ns


load_dotenv('.flaskenv')
load_dotenv('.env')


""" This is the main application that serves as the pivort and blueprint
    for other modules.All API endpoints would be defined here with route
    and views for the APIs to function.Also, this would serve other
    resources and modules.
"""


def create_app():
    """This method initialize and registers the app and the restful API
        including the namespaces
    """

    app = Flask(__name__)

    base_dir = os.path.dirname(os.path.realpath(__file__))

    # configure the SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('POSTGRES_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True

    # adding the secret
    app.config["JWT_SECRET_KEY"] = "super-secret"
    # initializing the JWTManager
    jwt.init_app(app)

    # creating and initializing the Login Manager instance class
    # login_manager = LoginManager(app)

    # register namespace Users
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(wallet_ns)
    api.add_namespace(pay_ns)

    api.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
