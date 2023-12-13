from cookbook import app, db
from cookbook.models import User, Recipes
from flask import render_template, Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template("home.html")


@routes.route('account')
def account():
    return render_template("account.html")