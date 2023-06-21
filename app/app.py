import os
from dotenv import load_dotenv
from app.controllers.controllers import *
from . import create_app

load_dotenv()

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.route("/")
def index():
    return "Hello, from task management!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
