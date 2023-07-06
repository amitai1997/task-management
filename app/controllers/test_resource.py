from flask_restful import Resource
import app


class MyResource(Resource):
    def get(self):
        a = app.url_map
        return {'message': 'Hello, world!'}
