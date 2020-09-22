from flask import Flask
import os


def create_app(test_config=None):

    # instance_relative_config connects the python app to the instance folder
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "bpdb.sqlite"),
    )

    # Imports the config information, ie: SECRET_KEY
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    # Creates the instance folder in the root dir if it doesn't exist yet
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def hello():
        return "hello, app"

    # Imports the db file and connects the functions
    from . import db

    db.init_app(app)

    # Imports and registers various blueprints
    from . import auth

    app.register_blueprint(auth.bp)

    return app