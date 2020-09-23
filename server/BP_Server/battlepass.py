import functools, os, datetime

from BP_Server.auth import verify_user

from flask import Blueprint, request, Response, json, current_app

from BP_Server.db import get_db

bp = Blueprint("battlepass", __name__, url_prefix="/bp")


@bp.route("/add", methods=["POST"])
def addRoute():
    # Finishing Add
    # 1) Don't allow duplicate names for user
    # 2) Finish Response Object

    user_check = verify_user(request)
    print(user_check)
    if user_check["status"] is False:
        return "Not a valid user"
    else:
        db = get_db()
        data = request.get_json()

        bpName = data["name"]
        currentXP = data["currentXP"]
        totalXP = data["totalXP"]
        endDate = data["endDate"]
        user_id = user_check["username"]

        db.execute(
            "INSERT INTO userPass (user_id, bpName, currentXP, totalXP, endDate) VALUES (?, ?, ?, ?, ?)",
            (
                user_id,
                bpName,
                currentXP,
                totalXP,
                endDate,
            ),
        )
        db.commit()

        return "still good"
