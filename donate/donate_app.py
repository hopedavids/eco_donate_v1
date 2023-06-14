import os
from flask import Flask
from dotenv import load_dotenv
from .exetensions import api, db
from .resources import auth_ns, user_ns, wallet_ns, pay_ns, trans_ns

load_dotenv('.flaskenv')


""" This is the main application that serves as the pivort and blueprint
    for other modules.All API endpoints would be defined here with route
    and views for the APIs to function.Also, this would serve other
    resources and modules.
"""

def create_app():
    app = Flask(__name__)

    base_dir = os.path.dirname(os.path.realpath(__file__))

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(base_dir, "donations.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['SQLALCHEMY_ECHO']=True

    # register Namespaces
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(wallet_ns)
    api.add_namespace(pay_ns)
    api.add_namespace(trans_ns)

    api.init_app(app)
    db.init_app(app)

    return app