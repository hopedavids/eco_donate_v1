import uuid
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from sqlalchemy import event, Boolean
from datetime import datetime
from .instances import db


"""In this model, all the schemas and tables,
    columns would be created here.
"""


class User(UserMixin, db.Model):
    """In this class, the data model for the User
        will be defined.
    """
    __tablename__ = 'donate_users'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, unique=True)
    email_confirm = db.Column(Boolean, default=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    email_confirm_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')
        return self.password
    
    def is_active(self):
        """True, as all users are active."""
        return True


    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def __str__(self):
        return {}.format(self.id)


class Wallet(db.Model):
    """This class defines the data model for the
        donate_wallet table.
    """

    def generate_wallet_id():
        return str(uuid.uuid4())

    __tablename__ = 'donate_wallets'

    wallet_id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('donate_users.id'), nullable=False, unique=True)
    current_balance = db.Column(db.Float, default=0.0)
    previous_balance = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', backref='wallet', uselist=False)


    def __str__(self):
        # The method show how the object should return in a human-readable format
        return {}.format(self.wallet_id)


class Payment(db.Model):
    """This object defines the data model and schemas
        for payments.
    """
    __tablename__ = 'donate_payments'

    payment_id = db.Column(db.Integer, primary_key=True)
    wallet_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('donate_wallets.wallet_id'), nullable=False)
    tree_species = db.Column(db.String(30), nullable=False)
    region_to_sow = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    get_certified = db.Column(Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    wallet = db.relationship('Wallet', backref='payment', uselist=False)


    def __str__(self):
        return {}.format(self.payment_id)



class Contact(db.Model):
    """This object handles the contact informations of 
        individual donors.
    """

    __tablename__ = 'donators_contact'

    contact_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('donate_users.id'), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    postal_code = db.Column(db.String(10), nullable=False)
    about_me = db.Column(db.String(255), nullable=False)

    user = db.relationship('User', backref='contact', uselist=False)


    def __str__(self):
        return {}.format(self.contact_id)




class Donation(db.Model):
    """This object defines the data model and schemas
        for donations.
    """

    __tablename__ = 'donations'

    donation_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, default=0.00)
    description = db.Column(db.String(255), nullable=False)




# This is method automatically updates the previous balance value
@event.listens_for(Wallet.current_balance, 'set')
def update_previous_balance(target, value, oldvalue, initiator):
    target.previous_balance = oldvalue
