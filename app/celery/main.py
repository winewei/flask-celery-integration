from app.celery import celery
from app.app import create_app
from app.config import settings
from app.celery.util import init_celery

app = create_app(settings)
init_celery(app=app, celery=celery)
