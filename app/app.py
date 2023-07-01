import os
from dotenv import load_dotenv, find_dotenv
from app.controllers.controllers import *
from . import create_app, redis_client


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.route("/")
def index():
    return "Hello, from task management!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
