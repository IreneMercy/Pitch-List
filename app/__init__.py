from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES
from dotenv import load_dotenv

load_dotenv()

app =  Flask(__name__)
mail=Mail(app)
db = SQLAlchemy(app)
loginmanager = LoginManager(app)
loginmanager.login_view = 'auth.login'
loginmanager.session_protection = 'strong'
photos = UploadSet('photos',IMAGES)
def create_app():
    app.config.from_object(Config)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    mail.init_app(app)
    configure_uploads(app,photos)
    return app
