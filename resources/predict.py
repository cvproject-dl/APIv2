from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from pytorch_helper.resnet34 import load_model, predict
from pytorch_helper.constants import MODEL_DIR
import os


class Predict(Resource):
    ALLOWED_EXTENTIONS = {'jpeg', 'jpg', 'png'}

    def __allowedfile(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in Predict.ALLOWED_EXTENTIONS

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument('image', type=FileStorage, location='files', required=True)
        args = parse.parse_args()
        image_file = args['image']
        print(image_file.filename)
        if image_file and self.__allowedfile(image_file.filename):
            try:
                filename = secure_filename(image_file.filename)
                loc = os.path.join('uploads', filename)
                image_file.save(loc)
                model = load_model(MODEL_DIR)
                res, total_cars = predict(model=model, fileloc=loc)
                os.remove(loc)
                return {'predictions': res, 'total_cars': total_cars, 'status': 200}, 200
            except Exception as e:
                return {"message": {'error': f"Internal Server Error {str(e)}", 'status': 500}}, 500

        else:
            return {"message": {'error': "Invalid Filename", 'status': 404}}, 404
