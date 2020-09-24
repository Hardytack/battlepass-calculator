import functools, os, datetime

from BP_Server.auth import verify_user

from flask import Blueprint, request, Response, json, current_app

from BP_Server.db import get_db

bp = Blueprint("battlepass", __name__, url_prefix="/bp")


# Finishing the Add Route
# - GET
# -- Return all Rows
# -- Return Single Requested Row
# - POST
# -- Finish Response Object


@bp.route("/user-bp", methods=["GET", "POST"])
def addRoute():
    # Verifies if user is authorized to access route
    user_check = verify_user(request)
    if user_check["status"] is False:
        my_response = Response(
            response=json.dumps({"error": "Not authorized to access this page"}),
            status=401,
            mimetype="application/json",
        )
        return my_response

    # Get Resources
    if request.method == "GET":
        if request.args.get("type") == "all":
            db = get_db()
            # Fetches all Battlepasses for user's id
            my_passes = db.execute(
                "SELECT * FROM userPass WHERE user_id = ?", (user_check["user_id"],)
            ).fetchall()
            # Maps all battlepasses to a list
            passes_list = []
            for x in my_passes:
                passes_list.append(list(x))
            my_response = Response(
                response=json.dumps({"data": passes_list}),
                status=200,
                mimetype="application/json",
            )
            return my_response
        elif request.args.get("type") is not None:
            return "you only want one?"
        return "loading...."

    # POST Resources
    else:
        db = get_db()
        data = request.get_json()

        bpName = data["name"]
        currentXP = data["currentXP"]
        totalXP = data["totalXP"]
        endDate = data["endDate"]
        user_id = user_check["user_id"]

        name_check = db.execute(
            "SELECT endDate FROM userPass WHERE user_id = ? AND bpName = ?",
            (user_id, bpName),
        ).fetchone()

        if name_check is not None:
            return "You already have run with this name"

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
