import os
import psycopg2
from flask import Flask, Blueprint, url_for
from dotenv import load_dotenv
from datetime import timedelta
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_restx import apidoc
from .instances import api, db, jwt, login_manager
from sqlalchemy.dialects.postgresql import psycopg2
from .resources import auth_ns, user_ns, wallet_ns, pay_ns, trans_ns, api_ns
from .user_auth import user_auth as user_auth_blueprint
from .main import main as main_blueprint


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

    
    # configure the SQLite database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('POSTGRES_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True


    # adding the secret to the app and JWT
    app.secret_key ="eudbefgeduegvd!@#"
    app.config["JWT_SECRET_KEY"] = "super-secret"

    # adding extra security parameters for sessions
    app.config['SESSION_COOKIE_SECURE'] = False
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
    csrf = CSRFProtect(app)
    # Use a secure session storage
    app.config['SESSION_TYPE'] = 'filesystem'
    Session(app)


    # initializing the JWTManager
    jwt.init_app(app)

    # creating and initializing the Login Manager instance class
    login_manager.init_app(app)

    # register namespace Users
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(wallet_ns)
    api.add_namespace(pay_ns)
    api.add_namespace(api_ns)

    api.init_app(app)
    db.init_app(app)
    
    # adding and registering the blueprint
    app.register_blueprint(user_auth_blueprint)
    app.register_blueprint(main_blueprint)

    @api.documentation
    def customize_swagger_ui():
        return {
            "basePath": "/api",  # Modify the base path here
            'info': {
                'title': 'My API',
                'version': '1.0',
            },
        }

    # API documentation route
    @app.route('/api/docs')
    def swagger_ui():
        return apidoc.ui_for(api)


    with app.app_context():
        db.create_all()

    return app
