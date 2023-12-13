from cookbook import app, db
from cookbook.models import User, Recipes
from flask import render_template, Blueprint
from flask_login import login_required, current_user

routes = Blueprint('routes', __name__)

@routes.route('/')
@login_required
def home():
    return render_template("home.html")


@routes.route('account')
@login_required
def account():
    return render_template("account.html")