import os
from dotenv import load_dotenv, find_dotenv
from app.controllers.controllers import *
from . import create_app
from flask_restful import Resource, Api


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
api = Api(app)


class IndexResource(Resource):
    def get(self):
        return "Hello, from task management!"


class RoutesResource(Resource):
    def get(self):
        """Print all routes and endpoints as JSON."""
        output = []
        for rule in app.url_map.iter_rules():
            methods = ','.join(rule.methods)
            line = {"endpoint": rule.endpoint, "methods": methods, "route": str(rule)}
            output.append(line)

        return output


api.add_resource(IndexResource, '/')
api.add_resource(RoutesResource, '/routes')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
