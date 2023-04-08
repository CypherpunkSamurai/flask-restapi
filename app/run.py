"""
Flask REST API for Twitter Clone

This is the main flask app.
"""
import os
from dotenv import load_dotenv
# flask
from flask import Flask

# routes
from posts import routs as post_routes
from weather import routs as weather_routes
from posts.models import db

# init logger
import utils

# Environment Variables
load_dotenv()

# Run Config
IS_DEBUG = os.getenv("DEBUG", 1)
CLEAN_START = os.getenv("CLEAN_START", False)

# Server Config
HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", 5000)


def create_app():
    """
    Flask App Factory to create app (recommended approach by flask)
    https://flask.palletsprojects.com/en/2.2.x/patterns/appfactories/

    :return:
    """
    app = Flask(__name__)

    # Blueprints
    app.register_blueprint(post_routes.b_new_post)
    app.register_blueprint(post_routes.b_get_post)
    app.register_blueprint(weather_routes.b_get_weather)

    # SQL Config
    app.config["SQLALCHEMY_DATABASE_URI"] = utils.POSTGRESQL_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = utils.IS_DEBUG

    # Context
    with app.app_context():
        db.init_app(app)
    return app


if __name__ == '__main__':
    # use factory to create app
    utils.logger.info("[app] creating app...")
    flask_app = create_app()

    # run the app
    if flask_app:
        utils.logger.info("[app] running app...")
        flask_app.run(host=HOST, port=PORT, debug=bool(IS_DEBUG))
