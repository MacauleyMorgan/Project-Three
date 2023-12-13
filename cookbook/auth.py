from cookbook import app
from flask import render_template, Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p>login function</p>"


@auth.route('/logout')
def logout():
    return "<p>logout function</p>"


@auth.route('/signup')
def signup():
    return "<p>signup function</p>"