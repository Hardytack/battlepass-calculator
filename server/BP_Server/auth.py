import functools

from flask import Blueprint, flash, g, redirect, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from BP_Server.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/hello")
def bp_test():
    return "you did it!"
