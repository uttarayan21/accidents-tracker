# 

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from accidents_db import db
from accidents_ui.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = True # Ignores trailing slashes

login_manager = LoginManager()
bcrypt = Bcrypt()


# Register Flask extensions
db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
from accidents_ui.users.routes import users
from accidents_ui.main.routes import main
from accidents_ui.database.routes import database

app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(database, url_prefix="/database")
