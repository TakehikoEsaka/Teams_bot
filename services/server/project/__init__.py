import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate


# instantiate the extensions
db = SQLAlchemy()
migrate = Migrate()


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # explicitly load .flaskenv (gnicornでproductionする時にも.flaskenv読みたい時は以下のように明示的に読む)
    # import os
    # from dotenv import load_dotenv
    # basedir = os.path.abspath(os.path.dirname('__file__'))
    # load_dotenv(os.path.join(basedir, '.flaskenv'))

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    # ？？flaskにdatabaseを覚えさせておく必要があるのか？？
    # from project.api.info import info_blueprint
    # app.register_blueprint(info_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
