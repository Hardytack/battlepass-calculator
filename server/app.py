from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

@app.route('/', methods=["GET"])
def text_route():
    return jsonify({"name": "python"})
app.run(debug=True)
