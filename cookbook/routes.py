from cookbook import app, db
from .models import User, Recipes
from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

routes = Blueprint('routes', __name__)


@routes.route('admin')
@login_required
def admin():
    """
    Function to display admin page, first user to sign up will automatically become an admin.
    """
    # Checks if user is first user (Change to admin boolean)
    if current_user.id == 1 and current_user.is_admin == False:
        current_user.is_admin = True
        db.session.commit()
        print(current_user.is_admin)
        return redirect(url_for('routes.admin'))
    elif current_user.is_admin == True:
        # If admin = True
        current_admins = list(User.query.order_by(User.is_admin == True).all())
        current_admin_names = []
        for admin in current_admins:
            if admin.is_admin:
                name = f"{admin.first_name} {admin.last_name}"
                current_admin_names.append(name)
                current_admin_names.sort()
        return render_template("admin.html", current_admin_names=current_admin_names)
    else:
        flash('You are not an admin', category = 'error')
        return render_template("home.html")


@routes.route('toggle_admin', methods=['GET','POST'])
@login_required
def toggle_admin():
    """
    Linked to form to enable/diables admin permissions on admin page, protects user with ID of 1 from losing permissions
    """ 
    if request.method == 'POST':
        email = request.form.get('user-email')
        checkbox = request.form.get('checkbox')
        # Check if email is valid
        user_exists = User.query.filter_by(email=email).first()
        # Function to change access level
        if user_exists and user_exists.id != 1:
            if checkbox == 'on':
                # User exists in database and access is given
                user_exists.is_admin = True
                print(user_exists.first_name, user_exists.is_admin)
                db.session.commit()
                flash('User is now an admin', category="success")
                return redirect(url_for('routes.admin'))
            elif checkbox == None:
                # User exists in database and access is removed
                print('User exists and would remove access')
                user_exists.is_admin = False
                db.session.commit()
                flash('User admin rights removed', category='info')
                return redirect(url_for('routes.admin'))
        elif user_exists.id == 1:
            flash('You can\'t remove owners permissions!')
            redirect(url_for('routes.admin'))
        else:
            # User does not exist in database
            flash('User does not exist', category='error')
    return render_template("admin.html")


@routes.route('/')
@login_required
def home():
    """
    Returns home page on site showing the communities recipes
    """
    recipes = list(Recipes.query.order_by(Recipes.name).all())
    return render_template("home.html", recipes=recipes)


# Function to load recipe page
@routes.route('recipes', methods=['GET', 'POST'])
@login_required
def recipes():
    """
    Displays recipes page on site, loads the recipes owned by the current user ID for modification/deletion
    """
    recipes = list(Recipes.query.order_by(Recipes.user_id).all())
    my_recipes = list()
    for recipe in recipes:
        if recipe.user_id == current_user.id:
            my_recipes.append(recipe)
        else:
            pass
    return render_template("recipes.html", recipes=my_recipes)


# Loads account page
@routes.route('account', methods=['GET', 'POST'])
@login_required
def account():
    """
    Renders account page
    """
    return render_template("account.html")


# User CRUD functions
# Change email
@routes.route('email_change/<int:current_user_id>', methods=['GET', 'POST'])
@login_required
def email_change(current_user_id):
    """
    Function to change email assocoated with account, checks if email is already in use before assigning it to the user
    """
    user = User.query.get_or_404(current_user_id)
    if request.method == 'POST':
        email = request.form.get('new-email')
        user_already_exists = User.query.filter_by(email=email).first()
        if user_already_exists:
            flash('Sorry, email is already in use', category="error")
            return redirect(url_for('routes.account'))
        else:
            user.email = email
            db.session.commit()
        return redirect(url_for('routes.account'))
    return render_template("account.html", user=user)


# Change password
@routes.route('password_change/<int:current_user_id>', methods=['GET', 'POST'])
@login_required
def password_change(current_user_id):
    """
    Allows usere to change password if they can confirm the previous password they have used, 
    If the current password matches the one in database, it will change it to the new password on submission
    """
    if request.method == 'POST':
        user = User.query.get_or_404(current_user_id)
        old_password = request.form.get('old-password')
        requested_password = request.form.get('new-password')
        if check_password_hash(user.password, old_password):
            if len(requested_password) > 3:
                new_password = generate_password_hash(requested_password, method='sha256')
                user.password = new_password
                db.session.commit()
                flash('Password successfully changed!', category='success')
                return redirect(url_for('routes.account'))
            else:
                flash('Password must be greater than 3 characters', category='error')
                return redirect(url_for('routes.account'))
        else:
            flash('Sorry, passwords do not match!', category='error')
            return redirect(url_for('routes.account'))
    return render_template("account.html", user=user)


# Function to delete recipes
@routes.route('delete_user/<int:current_user_id>', methods=['GET', 'POST'])
def delete_user(current_user_id): 
    """
    Takes user ID of current user
    Checks email written in form is equal to db storage as verification
    Deletes user account if emails match
    """
    user = User.query.get_or_404(current_user_id)
    if request.method == 'POST':
        # Checks email written into form to verify deletion
        verify = request.form.get('email')
        if user.email == verify:
            db.session.delete(user)
            db.session.commit()
            flash('Your account has been deleted')
            return redirect(url_for('auth.login'))
        else:
            flash('Sorry that did not work! Please try again')
            return redirect(url_for('routes.account'))
    return redirect(url_for('routes.account'))


# Recipe CRUD functions
# Edit Recipe
@routes.route('/edit_recipe/<int:recipe_id>', methods=['GET', 'POST'])
@login_required
def edit_recipe(recipe_id):
    """
    Takes recipe ID from card click on recipe page
    Loads current recipe into form
    On submission, overwrites db with form data supplied for recipe
    """
    find_recipe = Recipes.query.get_or_404(recipe_id)
    if current_user.is_admin == True or current_user.id == find_recipe.user_id:
        recipe = Recipes.query.get_or_404(recipe_id)
        if request.method == 'POST':
            recipe.name = request.form.get('recipe-name')
            recipe.recipe_time = request.form.get('recipe-time')
            recipe.recipe_image = request.form.get('recipe-image')
            recipe.recipe_ingredients = request.form.get('recipe-ingredients')
            recipe.recipe_steps = request.form.get('recipe-steps')
            db.session.commit()
            return redirect(url_for('routes.recipes'))
    else:
        flash('You do not have permissions to remove this recipe', category='error')
        return redirect(url_for('routes.home'))
    return render_template("edit_recipe.html", recipe=recipe)


# Function linked to form to submit recipe
@routes.route('/add_recipe', methods=['GET', 'POST'])
@login_required
def add_recipe():
    """
    Linked to add recipe page
    On posting the form the recipe is validated for character length in fields
    If pass, submit to database
    """
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
            recipe = Recipes(
                name=recipe_name, 
                recipe_time=recipe_time, 
                recipe_ingredients=recipe_ingredients, 
                recipe_image=recipe_image, 
                recipe_steps=recipe_steps, 
                user_id=current_user.id)
            db.session.add(recipe)
            db.session.commit()
            flash('Recipe uploaded successfully', category='success')
            return redirect(url_for('routes.recipes'))

    return render_template("add_recipe.html", user=current_user)


# Function to delete recipes
@routes.route('delete_recipe/<int:recipe_id>')
@login_required
def delete_recipe(recipe_id):
    """
    Deletes recipe clicked on by user from the recipes page
    """
    find_recipe = Recipes.query.get_or_404(recipe_id)
    if current_user.is_admin == True or current_user.id == find_recipe.owner:
        recipe = Recipes.query.get_or_404(recipe_id)
        db.session.delete(recipe)
        db.session.commit()
    else:
        print('You can not delete this')
    return redirect(url_for('routes.recipes'))


@routes.route('expand_recipe/<int:recipe_id>')
@login_required
def expand_recipe(recipe_id):
    """
    Lets user click on recipe on home page for expansion onto its own document
    """
    recipe_id = Recipes.query.get_or_404(recipe_id)
    recipe_owner = User.query.get_or_404(recipe_id.user_id)
    print(recipe_owner)
    return render_template('expand_recipe.html', recipe_id=recipe_id, recipe_owner=recipe_owner)


"""
Error handling section
"""

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
