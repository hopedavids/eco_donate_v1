from flask import Flask, jsonify
from flask_restx import Api, Resource, Namespace
from dotenv import load_dotenv

load_dotenv('.flasenv')


""" This is the main application that serves as the pivort and blueprint
    for other modules.All API endpoints would be defined here with route
    and views for the APIs to function.Also, this would serve other
    resources and modules.
"""


app = Flask(__name__)
api = Api(app)

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
