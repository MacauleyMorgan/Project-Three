from cookbook import app, db
from .models import User, Recipes
from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import login_required, current_user

routes = Blueprint('routes', __name__)

@routes.route('/')
@login_required
def home():
    return render_template("home.html")

# Function linked to form to submit recipe
@routes.route('/add_recipe', methods=['GET', 'POST'])
@login_required
def add_recipe():
    if request.method == 'POST':
        recipe_name = request.form.get('recipe-name')
        recipe_time = request.form.get('recipe-time')
        recipe_image = request.form.get('recipe-image')
        recipe_ingredients = request.form.get('recipe-ingredients')
        recipe_steps = request.form.get('recipe-steps')
        if len(recipe_name) < 1:
            flash('Recipe Name is too short!', category='error')
        elif len(recipe_image) < 1:
            flash('Recipe image link not provided', category='error')
        elif len(recipe_ingredients) < 1:
            flash('Recipe ingredients not provided', category='error')
        else: 
            recipe = Recipes(recipe_name=recipe_name, recipe_time=recipe_time, recipe_ingredients=recipe_ingredients, recipe_image=recipe_image, recipe_steps=recipe_steps, user_id=current_user.id)
            print(recipe)
            db.session.add(recipe)
            db.session.commit()
            return redirect(url_for('routes.recipes'))
            flash('Recipe uploaded succesfully', category='success')

    return render_template("add_recipe.html", user=current_user)


@routes.route('recipes', methods=['GET', 'POST'])
@login_required
def recipes():
    recipes = list(Recipes.query.order_by(Recipes).all())
    return render_template("recipes.html", recipes=recipes)


@routes.route('account', methods=['GET', 'POST'])
@login_required
def account():
    return render_template("account.html", recipes=recipes)