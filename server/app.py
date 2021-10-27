from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os

db_name = os.environ["DB_NAME"]
db_host = os.environ["DB_HOST"]
db_port = os.environ["DB_PORT"]
db_user = os.environ["DB_USER"]
db_password = os.environ["DB_PASSWORD"]

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"  # noqa E501
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models.group import Group  # noqa F401
from models.player import Player # noqa F401
from models.team import Team  # noqa F401

migrate = Migrate(app, db)
