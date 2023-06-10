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
ns = Namespace('Users', description="All user operations are handled here.") 

# register namespace Users
api.add_namespace(ns)


"""Below is the definition for the API routes and views """


@ns.route('/auth_user')
class Users(Resource):
    """This class object defines the routes and views for
       User Authentication.
    """

    def get(self):
        """ This method handles the GET HTTP method and return a response."""

        return jsonify({"hello":"world"})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
