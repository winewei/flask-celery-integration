# flask-celery-integration
This is a flask + celery demo, you can copy it.
## Requirements
- flask 2.2
- celery 5.2.7
- SQLAlchemy 1.4.44
- python >= 3.8 ?
- rabbitmq >= 3.11

## How To Use
- All in one
```shell
docker-compose up

curl http://localhost:5000/v1
curl http://localhost:5000/v1/get/{task_id}
```

- startup web app
```shell
pip install -r requirements.txt
export FLASK_APP=main.py
flask db upgrade
python main.py

curl http://localhost:5000/v1
curl http://localhost:5000/v1/get/{task_id}

```
- startup celery worker
```shell
celery --app app.celery.main:celery worker  --loglevel=info
```
