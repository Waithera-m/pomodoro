import os

class Config():

    '''
    class facilitates the creation of configuration objects
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mary:pixie01@localhost/pomodoro'
    UPLOADED_PHOTOS_DEST='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class DevConfig(Config):

    '''
    class inherits general configurations from Config class
    '''
    DEBUG = True

class ProdConfig(Config):

    '''
    class inherits general configurations from Config class
    '''
    pass

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}