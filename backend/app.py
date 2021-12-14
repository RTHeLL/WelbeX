# Import other modules
import os

# Import flask modules
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Configurations
DEBUG = True

# Aoo
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.urandom(24)

# DB configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://welbextz:123456@localhost:5432/welbextz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # Init DB for app
migrate = Migrate(app, db)  # Init migrate in DB from app

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

import models
