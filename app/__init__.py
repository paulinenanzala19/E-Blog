from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


bootstrap=Bootstrap()
db=SQLAlchemy()


def create_app(config_name):
    app=Flask(__name__)

    bootstrap.init_app(app)
    db.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)