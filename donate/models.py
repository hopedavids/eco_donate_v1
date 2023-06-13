from .donate_app import db


"""In this model, all the schemas and tables,
    columns would be created here.
"""


class User(db.Model):
    """In this class, the data model for the User
        will be defined.
    """

    __tablename__ = 'donate_users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, unique=True)
