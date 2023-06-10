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
        """ This method handles the GET HTTP method and return a response."""

        return jsonify({'hello': 'world'})

    def post(self):
        """This method handles the POST requests."""

        return jsonify({'Post': 'user'})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
