import os

class Config():

    '''
    class facilitates the creation of configuration objects
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')

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