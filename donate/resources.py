from flask_restx import Resource, Namespace
from .api_models import user_model, user_input_model
from .exetensions import db
from .models import User


authorizations = {
    "jsonWebToken": {
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}


# define namespace Users
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

    

@user_ns.route('')
class Users(Resource):
    """This class object defines the routes and views for
       User Authentication.
    """

    # method_decorators = ['jsonWebToken']

    @user_ns.doc(security="jsonWebToken")
    @user_ns.marshal_list_with(user_model)
    def get(self):
        """ This method handles the GET HTTP method and returns
            response in a serialized way.
        """
        user = User.query.all()
        return user

    @user_ns.expect(user_input_model)
    @user_ns.marshal_with(user_model)
    def post(self):
        """This method handles the POST and creates new uses based
            on requests.
        """

        print(user_ns.payload)
        user = User(
            username=user_ns.payload['username'], 
            email=user_ns.payload['email'], 
            password=user_ns.payload['password']
            )
        db.session.add(user)
        db.session.commit()

        return user, 201

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