import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

if os.path.exists("env.py"):
    import env # noqa

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
db = SQLAlchemy(app)

from cookbook.models import User
from cookbook.routes import routes # noqa
from cookbook.auth import auth # noqa

app.register_blueprint(routes, url_prefix="/")
app.register_blueprint(auth, url_prefix="/")

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))