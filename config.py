import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    DATABASE_PASS = os.environ.get('DATABASE_PASS')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moonguy:notmoonguy@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #  email configurations
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    DEBUG =True 

class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moonguy:notmoonguy@localhost/blog_test'
    DEBUG =True 

class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moonguy:notmoonguy@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
} 