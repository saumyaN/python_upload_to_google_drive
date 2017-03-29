import click
import os
from flask import Flask
from extensions import db

__name__ = 'googlesheets'

config = {
    "development": "settings.DevelopmentConfig",

}

engine = None


def create_app():
    click.echo("Creating App with name: %s" % __name__)
    app = Flask(__name__, instance_relative_config=True,
                instance_path=os.environ.get('FLASK_APP_INSTANCE_PATH'))
    print(app)
    setup_config(app)
    register_extensions(app)
    return app

def setup_config(app):
    environment = os.environ.get('APP_ENV', 'development')
    click.echo("Using environment: %s" % environment)
    app.config.from_object(config[environment])


def register_extensions(app):
    db.init_app(app)
    global engine
    engine = db.get_engine(app, bind='dgtech')
    print(engine)