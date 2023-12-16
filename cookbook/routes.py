from cookbook import app, db
from cookbook.models import User, Recipes
from flask import render_template, Blueprint, request, flash
from flask_login import login_required, current_user

routes = Blueprint('routes', __name__)

@routes.route('/')
@login_required
def home():
    return render_template("home.html")


@routes.route('account', methods=['GET', 'POST'])
@login_required
def account():
    if request.method == 'POST':
        recipe_name = request.form.get('recipe-name')
        recipe_time = request.form.get('recipe-time')
        recipe_image = request.form.get('recipe-image')
        recipe_ingredients = request.form.get('recipe-ingredients')
        recipe_steps = request.form.get('recipe-steps')
        recipe = [recipe_name, recipe_time, recipe_image, recipe_ingredients, recipe_steps]
        if len(recipe_name) < 1:
            flash('Recipe Name is too short!', category='error')
        elif len(recipe_image) < 1:
            flash('Recipe image link not provided', category='error')
        elif len(recipe_ingredients) < 1:
            flash('Recipe ingredients not provided', category='error')
        elif len(recipe_steps) < 1:
            flash('Recipe steps not provided', category='error')
        else: 
            new_recipe = Recipes(recipe, user_id=current_user.id)
            db.session.add(new_recipe)
            db.session.commit()
            flash('Recipe uploaded succesfully', category='success')
    return render_template("account.html", user=current_user)