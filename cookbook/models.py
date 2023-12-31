from cookbook import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """
    Model to manage users in the database
    """
    # Schema for the users of the site
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    # Mobile number is optional hence nullable true
    # treated as string incase of a + 44 entry etc
    mobile = db.Column(db.String, nullable=True)
    # Password not restricted in length due to password hashing
    password = db.Column(db.String, nullable=False)
    # Admin will automatically be false unless specified by db manager
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    # Keeps track of user recipes
    user_recipes = db.relationship(
        'Recipes', backref="user", cascade="all, delete", lazy=True)

    def __repr__(self):
        # represents itself as a string
        return (
            f"ID: {self.id} Name:{self.first_name}" +
            "{self.last_name} Email:{self.email}"
            )


class Recipes(db.Model):
    """
    Model for managing recipes
    """
    # Recipe id
    id = db.Column(db.Integer, primary_key=True)
    # Recipe name
    name = db.Column(db.String, nullable=False)
    # Recipe time, will specify intention to record time in minutes
    recipe_time = db.Column(db.Integer, nullable=False)
    # Recipe ingredients
    recipe_ingredients = db.Column(db.String, nullable=False)
    # Recipe steps
    recipe_steps = db.Column(db.String, nullable=False)
    # Image link to external source as a string
    recipe_image = db.Column(db.String, nullable=False)
    # Foreign key to link user
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        # represents itself as a string
        return (
            f"ID: {self.id} Name:{self.name}" +
            "Time:{self.recipe_time}" +
            "Ingredients:{self.recipe_ingredients" +
            "Steps:{self.recipe_steps} Owner: {self.user_id}")
