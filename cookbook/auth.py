from cookbook import app
from flask import render_template, Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>logout function</p>"


@auth.route('/signup')
def signup():
    return render_template("signup.html")