import os
from dotenv import load_dotenv, find_dotenv
from app.controllers.controllers import *
from . import create_app
from flask_restful import Resource
from flask_restful import Api


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
api = Api(app)


class IndexResource(Resource):
    def get(self):
        return "Hello, from task management!"


api.add_resource(IndexResource, '/')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
