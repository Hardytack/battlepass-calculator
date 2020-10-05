# Import modules needed for file
import sqlite3
import click

# current_app provides a reference to the currently running app
# g is a special object created for each request, it stores data that may be accessed several times during a request
from flask import current_app, g
from flask.cli import with_appcontext


# Fetches the database and adds it to the request context if not already there
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


# Checks if the db is current on the request object, and if it is, closed the connection
def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


# Initializes the DB
def init_db():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


# Adds the init-db command to the CLI
@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the Database")


# Adds the teardown and cli functions to the app
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)