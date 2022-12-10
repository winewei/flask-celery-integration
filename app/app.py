from flask import Flask
from app.celery.util import init_celery
from app.celery import celery
from app.extensions import db, migrate


def create_app(config_obj):
    app = Flask('app')
    app.config.from_object(config_obj)
    init_celery(app, celery)
    db.init_app(app)
    migrate.init_app(app, db)

    from .api.api import app as api_bp
    app.register_blueprint(api_bp, url_prefix="/v1")

    return app
