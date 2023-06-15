import uuid
from sqlalchemy import event
from datetime import datetime
from .instances import db


"""In this model, all the schemas and tables,
    columns would be created here.
"""


class User(db.Model):
    """In this class, the data model for the User
        will be defined.
    """
    __tablename__ = 'donate_users'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, unique=True)

    # wallet = db.relationship('Wallet', backref='user_wallet', uselist=False)


class Wallet(db.Model):
    """This class defines the data model for the
        donate_wallet table.
    """

    def generate_wallet_id():
        return str(uuid.uuid4())

    __tablename__ = 'donate_wallets'

    wallet_id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('donate_users.id'), nullable=False)
    current_balance = db.Column(db.Float, default=0.0)
    previous_balance = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', backref='wallet', uselist=False)

# @event.listens_for(User, 'after_insert')
# def create_wallet(mapper, connection, target):
#     wallet = Wallet(user_id=target.id)
#     db.session.add(wallet)
#     db.session.commit()


class Payment(db.Model):
    """This object defines the data model and schemas
        for payments.
    """
    __tablename__ = 'donate_payments'

    payment_id = db.Column(db.Integer, primary_key=True)
    wallet_id = db.Column(db.UUID(as_uuid=True), db.ForeignKey('donate_wallets.wallet_id'), nullable=False)
    donation_id = db.Column(db.Integer, db.ForeignKey('donations.donation_id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    wallet = db.relationship('Wallet', backref='payment', uselist=False)
    donation = db.relationship('Donation', backref='payment', uselist=False)


class Donation(db.Model):
    """This object defines the data model and schemas
        for donations.
    """

    __tablename__ = 'donations'

    donation_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, default=0.00)
    description = db.Column(db.String(255), nullable=False)
