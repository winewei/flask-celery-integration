# flask-celery-integration
This is a flask + celery demo, you can copy it.
## Requirements
- flask 2.2
- celery 5.2.7
- SQLAlchemy 1.4.44
- python >= 3.8 ?
- rabbitmq >= 3.8

## How To Use
- startup web app
```shell
pip install -r requirements.txt
export FLASK_APP=main.py
flask db upgrade
python main.py
```
- startup celery worker
```shell
celery --app app.celery.main:celery worker  --loglevel=info
```
