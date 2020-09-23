import functools, os, datetime

import jwt

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
    current_app,
)
from werkzeug.security import check_password_hash, generate_password_hash

from BP_Server.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")


def generate_token(user_id):
    try:
        payload = {
            "exp": datetime.datetime.utcnow()
            + datetime.timedelta(days=0, minutes=10, seconds=5),
            "iat": datetime.datetime.utcnow(),
            "sub": user_id,
        }
        return jwt.encode(
            payload, current_app.config.get("SECRET_KEY"), algorithm="HS256"
        )
    except Exception as e:
        return e


def decode_token(auth_token):
    try:
        payload = jwt.decode(auth_token, current_app.config.get("SECRET_KEY"))
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        return "Signature expired. Please log in again"
    except jwt.InvalidTokenError:
        return "Invalid token. Please try again"


def verify_user(user_request):
    db = get_db()
    auth_header = user_request.headers.get("Authorization")
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ""
    if auth_token:
        decoded_token = decode_token(auth_token)
        print(decoded_token)
        if not isinstance(decoded_token, str):
            user = db.execute(
                "SELECT * FROM users WHERE id = ?", (decoded_token,)
            ).fetchone()
            if user is not None:
                return True
    return False


@bp.route("/login", methods=["POST"])
def login():
    db = get_db()
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
        auth_token = generate_token(user["id"])
        my_response = Response(
            response=json.dumps(
                {
                    "message": "user logged in!",
                    "auth_token": auth_token.decode(),
                    "username": user["username"],
                }
            ),
            status=200,
            mimetype="application/json",
        )
        return my_response
    else:
        my_response = Response(
            response=json.dumps(error), status=500, mimetype="application/json"
        )
        return my_response


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
        user = db.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        auth_token = generate_token(user["id"])
        my_response = Response(
            response=json.dumps(
                {
                    "message": "user created!",
                    "auth_token": auth_token.decode(),
                    "username": user["username"],
                }
            ),
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

    # # Verifying if an input is in a list
    # content = request.get_json()
    # name = content["username"]
    # my_names = ["hardy", "sarah", "astrid"]
    # if name in my_names:
    #     return "its here!"
    # else:
    #     return "not in the list"

    # db = get_db()
    # my_token = generate_token(3)
    # print(my_token)
    # decoded = decode_token(my_token)
    # print(decoded)

    # user = db.execute("SELECT * FROM users WHERE id = ?", (decoded,)).fetchone()

    # if user is not None:
    #     print(user["username"])
    # else:
    #     print("not found")

    # return "check console"
    result = verify_user(request)
    if result:
        return "you're good!"
    else:
        return "nana"
