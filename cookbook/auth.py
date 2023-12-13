from cookbook import app
from flask import render_template, Blueprint, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        """
        This will action when button is clicked to login
        """
        email = request.form.get('email')
        password = request.form.get('password')
        submission = [email, password]
        print(submission)
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>logout function</p>"


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
        user = [first_name, last_name, mobile, email, password1, password2]
        print(user)
    return render_template("signup.html")