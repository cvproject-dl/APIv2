from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from dbmodels.initdb import db
from resources import Predict, GetCars, Root

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

api = Api(app=app)

# initialize database
db.init_app(app)

api.add_resource(Root, '/')
api.add_resource(Predict, '/predict')
api.add_resource(GetCars, '/cars')

if __name__ == '__main__':
    app.run()
