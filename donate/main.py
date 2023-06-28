import os
from dotenv import load_dotenv
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime
from .instances import db
from .models import Wallet, Donation, Contact, Payment


main = Blueprint('main', __name__)

load_dotenv('.env')


@main.route('/profile', methods = ['GET', 'POST'])
@login_required
def index():
    # derive the user id from the user session
    user_id = current_user.id

    user = current_user.username
    user_email = current_user.email
    user_creation = current_user.created_date
    created_user_format = user_creation.strftime("%B %d, %Y %H:%M:%S")

    

    wallet = Wallet.query.filter_by(user_id=user_id).first()
    wallet_id = wallet.wallet_id
    current_balance = wallet.current_balance
    previous_balance = wallet.previous_balance

    created_at = wallet.created_at
    created_date_format = created_at.strftime("%B %d, %Y %H:%M:%S")
    
    updated_at = wallet.updated_at
    updated_date_format = updated_at.strftime("%B %d, %Y %H:%M:%S")

    if request.method == 'POST':
        amount = request.form['amount']
        region = request.form['region']
        tree_spieces = request.form['spieces']
        description = request.form['description']
        get_certified = request.form.get('get_certified', False)

        number_of_trees = amount
        minimum_length = 20

        # contact details
        fullname = request.form['fullname']
        address = request.form['address']
        country = request.form['country']
        about_me = request.form['aboutme']
    
        if any(len(text) < minimum_length for text in ([description, about_me])):
            flash("description should be more than 20 words", 'danger')
            return redirect(url_for("main.index"))

        if (not fullname or not address or not country or not about_me or not description):
            flash('kindly fill all fields correctly', 'danger')
            return redirect(url_for("main.index"))
        
        if any(text.isupper() for text in [fullname,country, address, about_me, description]):
            flash("kindly use alphanumeric or lowercase", 'danger')
            return redirect(url_for("main.index"))

        
        if amount:
            # check if amount is matches or less than the wallet balance
            if float(amount) > current_balance:
                flash("Dear Donor, you have insufficient Fund in your account", 'warning')
                return redirect(url_for("main.index"))
            
        # make the donotion happen
        current_balance -= float(amount)
        wallet.current_balance = current_balance

        donation = Donation(
                        user_id=user_id, 
                        amount=amount,
                        region_to_plant=region,
                        tree_spieces=tree_spieces,
                        number_of_trees=number_of_trees,
                        description=description
                        )

        contact = Contact(
                        user_id=user_id,
                        full_name=fullname,
                        address=address,
                        country=country,
                        about_me=about_me
                        )

        db.session.add_all([wallet, donation, contact])
        db.session.commit()

        # query the donation object to retrieve the id
        donation = Donation.query.filter_by(user_id=user_id).first()

        donate_wallet = os.environ.get('DONATE_WALLET')
        payment = Payment(
                    wallet_id=donate_wallet, 
                    amount=amount, 
                    donation_id=donation.donation_id
                    )

        wallet=Wallet.query.filter_by(wallet_id=donate_wallet).first()
        wallet.current_balance = amount

        db.session.add_all([payment, wallet])
        db.session.commit()

        

        flash("Congratulations! Your tree planting donations was successful!!", 'success')

        return redirect(url_for('main.gratitude'))

    
    return render_template('backend/index.html', 
                            user=user,
                            email=user_email,
                            created_date=created_user_format,
                            wallet_id=wallet_id,
                            current_balance=current_balance,
                            previous_balance=previous_balance,
                            created_at=created_date_format,
                            updated_at=updated_date_format
                            )



@main.route('/transactions')
@login_required
def transaction():
    page = request.args.get('page', 1, type=int)
    user_id = current_user.id
    contacts = Contact.query.filter_by(user_id=user_id).paginate(page=page, per_page=2)
    donations = Donation.query.filter_by(user_id=user_id).paginate(page=page, per_page=2)
    payments = Payment.query.filter_by(wallet_id=os.environ.get('DONATE_WALLET')).paginate(page=page, per_page=2)

    wallets = Wallet.query.filter_by(user_id=user_id).paginate(page=page, per_page=2)
    print(dir(wallets))
    print(wallets.items)
    print(wallets.page)

    transaction = zip(wallets, payments)

    data = zip(donations, contacts)


    return render_template('backend/pages/tables.html', data=data, transactions=transaction)


@main.route('/thank-you')
@login_required
def gratitude():
    
    user = current_user.username

    return render_template('backend/pages/thank-you.html', user=user)

