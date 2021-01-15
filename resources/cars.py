from flask_restful import Resource, reqparse
from dbmodels import Cars


class GetCars(Resource):
    def get(self):
        parse = reqparse.RequestParser()
        parse.add_argument('page', type=int)
        parse.add_argument('search')
        args = parse.parse_args()
        page = args['page']
        search_term = args['search']
        try:
            res = Cars.get_items(page=page) if search_term is None else Cars.search_by_name(
                search_term=search_term,
                page=page)
            if len(res) > 0:
                val = {'cars': res, 'status': 200, 'invalidPage': False}, 200
            else:
                val = {'cars': res, 'status': 400, 'invalidPage': True}, 400
            return val
        except Exception as e:
            return {"message": {'error': f"Internal Server Error {str(e)}", 'status': 500}}, 500
