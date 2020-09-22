import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    request,
    session,
    url_for,
    Response,
    jsonify,
    json,
)
from werkzeug.security import check_password_hash, generate_password_hash

from BP_Server.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["POST"])
def login():
    content = request.get_json()
    username = content["username"]
    password = content["password"]
    error = None

    user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

    if user is None:
        error = {"message": "Username and/or Password are incorrect"}
    elif not check_password_hash(user["password"], password):
        error = {"message": "Username and/or Password are incorrect"}

    if error is None:
        session.clear()


@bp.route("/register", methods=["POST"])
def register():
    content = request.get_json()
    username = content["username"]
    password = content["password"]
    db = get_db()
    error = None

    if not username:
        error = "Username is required."
    elif not password:
        error = "Password is required."
    elif (
        db.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()
        is not None
    ):
        error = {"message": f"User {username} is already registered."}

    if error is None:
        db.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, generate_password_hash(password)),
        )
        db.commit()
        my_response = Response(
            response=json.dumps({"message": "user created!"}),
            status=201,
            mimetype="application/json",
        )
        return my_response
    else:
        my_response = Response(
            response=json.dumps(error), status=500, mimetype="application/json"
        )
        return my_response


# Test Route
@bp.route("/hello", methods=["GET", "POST"])
def bp_test():

    # Verifying if an input is in a list
    content = request.get_json()
    name = content["username"]
    my_names = ["hardy", "sarah", "astrid"]
    if name in my_names:
        return "its here!"
    else:
        return "not in the list"
