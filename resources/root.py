from flask_restful import Resource


class Root(Resource):
    def get(self):
        return {'prediction': '/predict', 'list_of_cars': '/cars'}, 200
