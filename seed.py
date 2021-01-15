"""
To insert car details to the database.
Delete this package before deploying.

"""

from flask import Flask
from dbmodels.initdb import db
from seeder import cars_seeder


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize database

db.init_app(app)

with app.app_context():
    db.create_all()
    cars_seeder('class_names/car_seed_data.json')
