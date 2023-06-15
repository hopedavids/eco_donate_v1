from flask import jsonify
from flask_restx import Resource, Namespace
from flask_jwt_extended import jwt_required
from .instances import db
from .models import User


"""In this module, namespaces are defined and including the routes and views
    which are also defined here and associated with the models module.
"""


authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}

# define namespaces for the views
auth_ns = Namespace('authenticate', description="Login Endpoint")
user_ns = Namespace('user', description="All user operations.", authorizations=authorizations)
wallet_ns = Namespace('wallet', description="Wallet information")
pay_ns = Namespace('payment', description="All payments operations")
trans_ns = Namespace('transaction', description="Transactions operation")


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


@jwt_required
@user_ns.route('')
class Users(Resource):
    """This class object defines the routes and views for
       User Authentication.
    """
    method_decorator = ['jsonWebToken']

    @user_ns.doc(security="jsonWebToken")
    def get(self):
        """ This method handles the GET HTTP method and returns
            response in a serialized way.
        """

        user = User.query.all()

        return jsonify({'username': user})

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
