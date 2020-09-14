from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize App
app = Flask(__name__)
# App Routes
@app.route("/", methods=["GET"])
def text_route():
    return jsonify({"name": "python"})


# Run App
if __name__ == "__main__":
    app.run(debug=True)
