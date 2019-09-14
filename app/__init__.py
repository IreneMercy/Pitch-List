from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app =  Flask(__name__)
db = SQLAlchemy(app)
loginmanager = LoginManager(app)
loginmanager.login_view = 'auth.login'
loginmanager.session_protection = 'strong'

def create_app():
    app.config.from_object(Config)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    return app
