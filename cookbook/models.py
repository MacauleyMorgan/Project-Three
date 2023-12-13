from cookbook import db

class User(db.Model):
    # Schema for the users of the site
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    # Mobile number is optional hence nullable true, treated as string incase of a +44 entry etc
    mobile = db.Column(db.String, nullable=True)
    # Password not restricted in length due to password hashing
    password = db.Column(db.String, nullable=False)
    # Admin will automatically be false unless specified by db manager
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    user_recipes = db.relationship("Recipes", backref="user", cascade="all, delete", lazy=True)

    def __repr__(self):
        # represents itself as a string
        return f"ID: {self.id} Name:{self.first_name} {self.last_name}"


class Recipes(db.Model):
    # Schema for recipes of each user
    id = db.Column(db.Integer, primary_key=True)
    # Recipe name is not unique due to plan to add Account name on end of entry on the front end
    recipe_name = db.Column(db.String, db.ForeignKey('user.email', ondelete='CASCADE'), nullable=False)
    # Recipe time, will specify intention to record time in minutes
    recipe_time = db.Column(db.Integer, nullable=False)
    recipe_ingredients = db.Column(db.String, nullable=False)
    recipe_steps = db.Column(db.String, nullable=False)

    def __repr__(self):
        # represents itself as a string
        return f"ID:{self.id} Recipe:{self.recipe_name} Time:{self.recipe_time} Ingredients:{self.recipe_ingredients} Steps:{self.recipe_steps}"
