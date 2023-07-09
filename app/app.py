import os
from dotenv import load_dotenv, find_dotenv
from app.controllers.controllers import *
from . import create_app
from flask_restful import Resource, Api
from datetime import datetime, timedelta

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
api = Api(app)


class IndexResource(Resource):
    def get(self):
        from . import r
        # return "Hello, from task management!"
        # Get the client's IP address (you can use other identifiers as well)
        client_ip = request.remote_addr

        # Generate a unique key for the client's rate limit data
        rate_limit_key = f"rate_limit:{client_ip}"

        # Check if the rate limit key exists in Redis
        if r.exists(rate_limit_key):
            # Get the current request count and the timestamp of the first request within the time window
            request_count, first_request_time = r.hmget(rate_limit_key, 'count', 'timestamp')
            request_count = int(request_count)

            # Calculate the elapsed time since the first request
            elapsed_time = datetime.now() - datetime.strptime(first_request_time, '%Y-%m-%d %H:%M:%S.%f')

            # Check if the elapsed time exceeds the rate limit period
            if elapsed_time > timedelta(seconds=app.config['RATE_LIMIT_PERIOD']):
                # Reset the rate limit timestamp for the client
                first_request_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                request_count = 0
                r.hmset(rate_limit_key, {'count': request_count, 'timestamp': first_request_time})
            else:
                # Check if the request count exceeds the rate limit
                if request_count >= app.config['RATE_LIMIT']:
                    return jsonify({'error': 'Rate limit exceeded'})

        else:
            # Create rate limit data for the client
            request_count = 0
            first_request_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            r.hmset(rate_limit_key, {'count': request_count, 'timestamp': first_request_time})

        # Increment the request count for the client
        r.hincrby(rate_limit_key, 'count', 1)

        # Process the request normally
        return jsonify({'message': 'Request processed successfully'})


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
