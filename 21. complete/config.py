import os

DBURI = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
 #   SECRET_KEY = "Thismustbesecret"

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DBURI
 #   SECRET_KEY = os.environ["SECRET_KEY"]

class DevelopmentConfig(Config):
    DEBUG = True
