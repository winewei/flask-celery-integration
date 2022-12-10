from celery import Celery

celery = Celery('app', config_source='app.celery.config')
