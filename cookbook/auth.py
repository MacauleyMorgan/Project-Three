from cookbook import app, db
from flask import render_template, Blueprint, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        """
        This will action when button is clicked to login
        """
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Check if email exists
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Successful log in!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('routes.home'))
            else:
                flash('Incorrect password!', category='error')
        else:
            flash('Email is not in database!', category='error')
    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        """
        This will action when button is clicked to register
        """
        first_name = request.form.get('fname')
        last_name = request.form.get('lname')
        mobile = request.form.get('mobile')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user_already_exists = User.query.filter_by(email=email).first()
        if user_already_exists:
            flash('An account already exists using this email!', category='error')
        elif len(first_name) < 2:
            flash('Your first name must be longer than 1 letter', category='error')
        elif len(last_name) < 2:
            flash('Your last name must be longer than 1 letter', category='error')
        elif password1 != password2:
            flash('Passwords do not match!', category='error')
        elif len(password1) < 3:
            flash('Your password should be longer than 3 characters!')
        else:
            new_user = User(first_name=first_name, last_name=last_name, mobile=mobile, email=email, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            return redirect(url_for('routes.home'))
            flash('Welcome aboard!', category='success')
    return render_template("signup.html")