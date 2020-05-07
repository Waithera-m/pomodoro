from flask_bootstrap import Bootstrap
from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_wtf.csrf import CSRFProtect

csrf=CSRFProtect()

photos=UploadSet('photos',IMAGES)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.signin'

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):

    '''
    application factory facilitates app and extensions initializaton and blueprint registration
    '''

    app=Flask(__name__)

    #app configurations
    app.config.from_object(config_options[config_name])

    #extension initialization
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    #configure uploadset
    configure_uploads(app,photos)

    #blueprint registration
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

    return app