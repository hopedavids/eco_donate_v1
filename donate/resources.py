from flask import jsonify, request
from flask_restx import Resource, Namespace
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash
from .instances import db, login_manager, csrf, api
from .api_models import user_model, user_creation_model, wallet_model, payment_model, contact_model, donation_model
from .models import User, Wallet, Payment, Contact, Donation


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
contact_ns = Namespace('contact', description="All Contact informations")
donation_ns = Namespace('donation', description="Donations operation")
api_ns = Namespace('api', description='API namespace')





@login_manager.user_loader
def load_user(user_id):
    return User.query.get((user_id))



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


@user_ns.route('/get_user')
class Users(Resource):
    """This class object defines the routes and views for
       User Authentication.
    """

    # @user_ns.doc(security="jsonWebToken")
    @user_ns.marshal_list_with(user_model)
    # @jwt_required()
    def get(self):
        """ This method handles the GET HTTP method and returns
            response in a serialized way.
        """

        user = User.query.all()

        return user, 200

  
    @user_ns.expect(user_creation_model)
    def post(self):
        """This method handles the POST and creates new uses based
            models defined.
        """
        # Access the request payload data using `request.get_json()`
        payload = request.get_json()
        
        # Validate the payload data against the user_creation_model
        if not api.payload:
            return {'message': 'Invalid payload'}, 400
        
        # Extract the data from the payload using marshal
        username = api.payload.get('username')
        email = api.payload.get('email')
        password = api.payload.get('password')

        # hashed the plain text password with the generate_password_hash method
        hashed_password = generate_password_hash(password, method='sha256')

        # inject the data into the User object
        user = User(username=username, email=email, password=hashed_password)
        
        # save the new instance into the database
        db.session.add(user)
        db.session.commit()

        # return successful message once passed
        return {'message': 'User created successfully'}, 201


    def put(self):
        """This method updates a user details and roles"""

        pass



@user_ns.route('/<int:id>')
class Users(Resource):
    """This class object defines the routes and views for
       User Authentication.
    """

    @user_ns.marshal_list_with(user_model)
    def get(self, id):
        """ This method handles the GET HTTP method and returns
            response in a serialized way.
        """
        #query the user object
        user = User.query.filter_by(id=id).first()

        return user, 200
    
    

@wallet_ns.route('/all-wallets')
class Wallet_Details(Resource):
    """This object defines the routes and views for Wallet and
        handles all wallets resources.
    """

    @wallet_ns.marshal_list_with(wallet_model)
    def get(self):
        """The get method handles the HTTP GET requests and returns
            response in a serialized way.
        """

        wallet = Wallet.query.all()
        return wallet

    def post(self):
        """This method provides the means to create new wallets."""

        pass

    def put(self):
        """This method provides the flexibility to update user's
            wallet details.
        """

        pass


@pay_ns.route('/all-payments')
class Payment_Info(Resource):
    """This object defines the routes and views for Payment and
        handles the defined resources.
    """
    @pay_ns.marshal_list_with(payment_model)
    # @jwt_required()
    def get(self):
        """This method handles the HTTP GET method and provides the
            platform to retrieve payments informations.
        """

        payment = Payment.query.all()

        return payment

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


@contact_ns.route('/all-contacts')
class Contact_Details(Resource):
    """This object defines views for Contact and
        handles the defined resources.
    """

    @contact_ns.marshal_list_with(contact_model)
    def get(self):
        """This method handles the HTTP GET method and provides the
            platform to retrieve payments informations.
        """

        contact = Contact.query.all()
        return contact



@donation_ns.route('/all-donations')
class Donations(Resource):
    """This object defines the routes and views for Donations and
        handles the defined resources.
    """

    @donation_ns.marshal_list_with(donation_model)
    def get(self):
        """This method handles the HTTP GET method and provides the
            platform to retrieve donations.
        """

        donation = Donation.query.all()

        return donation