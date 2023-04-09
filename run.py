"""
Flask REST API for Twitter Clone

This is the main flask app.
"""
import os
# flask
from flask import Flask

# routes
from posts import routs as post_routes
from weather import routs as weather_routes
from posts.models import db

# init logger
import utils

# Run Config


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
        # bind context
        db.init_app(app)

        # clean the database
        if utils.CLEAN_START:
            db.create_all()
            utils.add_function(db)

    return app


if __name__ == '__main__':
    # use factory to create app
    utils.logger.info("[app] creating app...")
    flask_app = create_app()

    # run the app
    if flask_app:
        utils.logger.info("[app] running app...")
        flask_app.run(host=HOST, port=PORT, debug=bool(utils.   IS_DEBUG))
