import os
from flask import Flask, jsonify, request
from flask_restx import Api, Resource, Namespace
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_login import LoginManager, login_user, logout_user, login_required

load_dotenv('.flaskenv')


""" This is the main application that serves as the pivort and blueprint
    for other modules.All API endpoints would be defined here with route
    and views for the APIs to function.Also, this would serve other
    resources and modules.
"""


app = Flask(__name__)
api = Api(app)

# creating and initializing the Login Manager instance class
login_manager = LoginManager(app)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///donations.db"

#initialize the app with the extension
db = SQLAlchemy(app)


# define namespace Users
auth_ns = Namespace('authenticate', description="Login Endpoint")
user_ns = Namespace('user', description="All user operations.")
wallet_ns = Namespace('wallet', description="Wallet information")
pay_ns = Namespace('payment', description="All payments operations")
trans_ns = Namespace('transaction', description="Transactions operation")

# register namespace Users
api.add_namespace(auth_ns)
api.add_namespace(user_ns)
api.add_namespace(wallet_ns)
api.add_namespace(pay_ns)
api.add_namespace(trans_ns)


"""Below is the definition for the API routes and views """


@auth_ns.route('')
class Authentication(Resource):
    """ Login Endpoint to access the endpoint and api resources.
        This allows users to retrieve a JWT which gives access
        to all eco_donate resources
    """

    def post(self):
        """ This allows users to retrieve a JWT which gives access.
        """
        
        pass
    
    @login_manager.user_loader
    def load_user(user_id):
        return users.get(int(user_id))

    def login():
        """ This is the login session to authenticate users.
        """
        
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # authenticate the user using the in-built authenticate_user method
        authenticated_user = authenticate_user(username, password)

        if authenticated_user:
            login_user(authenticated_user)
            # generate token after a successful login
            token = generate_token(authenticated_user)
            return jsonify({'token': token}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401


@user_ns.route('/<int:id>')
class Users(Resource):
    """This class object defines the routes and views for
       User Authentication.
    """

    def get(self):
        """ This method handles the GET HTTP method and returns
            response in a serialized way.
        """

        return jsonify({'hello': 'world'})

    def post(self):
        """This method handles the POST and creates new uses based
            on requests.
        """

        return jsonify({'Post': 'user'})

    def put(self):
        """This method updates a user details and roles"""

        pass


@wallet_ns.route()
class Wallet(Resource):
    """This object defines the routes and views for Wallet and
        handles all wallets resources.
    """

    def get(self):
        """The get method handles the HTTP GET requests and returns
            response in a serialized way.
        """

        pass

    def post(self):
        """This method provides the means to create new wallets."""

        pass

    def put(self):
        """This method provides the flexibility to update user's
            wallet details.
        """

        pass


@pay_ns.route()
class Payment(Resource):
    """This object defines the routes and views for Payment and
        handles the defined resources.
    """

    def get(self):
        """This method handles the HTTP GET method and provides the
            platform to retrieve payments informations.
        """

        pass

    def post(self):
        """This method handles the HTTP POST requests and provides the
            platform to create new payment.
        """

        pass

    def put(self):
        """This method handles the HTTP PUT requests and provides the
            platform to update payment based on id.
        """

        pass


@trans_ns.route()
class Transaction(Resource):
    """This object defines the routes and views for Transactions and
        handles the defined resources.
    """

    def get(self):
        """This method handles the HTTP GET method and provides the
            platform to retrieve transactions details.
        """

        pass


if __name__ == "__main__":
    app.run(host='0.0.0.0')
