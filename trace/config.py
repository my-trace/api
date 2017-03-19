import os

class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ['DEV_DB_URL']
    APP_ID = os.environ['APP_ID']
    APP_SECRET = os.environ['APP_SECRET']
    APP_TOKEN = os.environ['APP_TOKEN']

class Test(Config):
    ENV = 'test'
    ANDY_TOKEN = os.environ.get('ANDY_TOKEN')

class Development(Config):
    ENV = 'development'
    DEBUG = True

class Production(Config):
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.environ['PROD_DB_URL']
