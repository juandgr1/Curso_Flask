from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("config.ProductionConfig")
db = SQLAlchemy(app)

from app.routes import *
