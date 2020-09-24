import functools, os, datetime

from BP_Server.auth import verify_user

from flask import Blueprint, request, Response, json, current_app

from BP_Server.db import get_db

bp = Blueprint("battlepass", __name__, url_prefix="/bp")


# Finishing the Add Route
# - PATCH
# -- Update DB entry with new information
# - DELETE
# -- Delete requested row


@bp.route("/user-bp", methods=["GET", "POST", "PATCH", "DELETE"])
def addRoute():
    # Verifies if user is authorized to access route
    user_check = verify_user(request)
    if user_check["status"] is False:
        return Response(
            response=json.dumps({"error": "Not authorized to access this page"}),
            status=401,
            mimetype="application/json",
        )

    # Setup DB for later functions
    db = get_db()
    data = request.get_json()

    # Get Resources
    if request.method == "GET":

        # Fetches all Battlepasses for user's id
        if request.args.get("type") == "all":
            my_passes = db.execute(
                "SELECT * FROM userPass WHERE user_id = ?", (user_check["user_id"],)
            ).fetchall()

            # Maps all battlepasses to a list
            passes_list = []
            for x in my_passes:
                passes_list.append(list(x))

            # Returns response object
            return Response(
                response=json.dumps({"data": passes_list}),
                status=200,
                mimetype="application/json",
            )

        # Fetches only requested battlepass via id
        elif request.args.get("bpid") is not None:
            my_pass = db.execute(
                "SELECT * FROM userPass WHERE id = ?", (request.args.get("bpid"),)
            ).fetchone()
            if my_pass is not None:
                return Response(
                    response=json.dumps({"data": list(my_pass)}),
                    status=200,
                    mimetype="application/json",
                )
            else:
                return Response(
                    response=json.dumps({"error": "Battlepass not found"}),
                    status=404,
                    mimetype="application/json",
                )
        else:
            return Response(
                response=json.dumps(
                    {"error": "Please include either a type or dbid query parameter"}
                ),
                status=404,
                mimetype="application/json",
            )

    # POST Resources
    elif request.method == "POST":
        bpName = data["name"]
        currentXP = data["currentXP"]
        totalXP = data["totalXP"]
        endDate = data["endDate"]
        user_id = user_check["user_id"]

        # Verifies the user doesn't already have an entry with this name
        name_check = db.execute(
            "SELECT endDate FROM userPass WHERE user_id = ? AND bpName = ?",
            (user_id, bpName),
        ).fetchone()

        if name_check is not None:
            return Response(
                response=json.dumps(
                    {"message": "You already have a battlepass with this name"}
                ),
                status=400,
                mimetype="application/json",
            )

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

        return Response(
            response=json.dumps({"message": "Added Successfully"}),
            status=201,
            mimetype="application/json",
        )

    # Placeholder for PATCH and DELETE
    else:
        return "Route not valid yet"
