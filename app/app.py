from flask import Flask
from app.config import *

app = Flask(__name__)

from app.controllers.billing_controller import billing_bp

# Register blueprints
app.register_blueprint(billing_bp)


@app.route("/")
def index():
    return "Hello, from alfabeitproj2!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
