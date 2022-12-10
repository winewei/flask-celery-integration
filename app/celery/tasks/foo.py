from .. import celery as celery_app
from app.extensions import db
from app.models import UserModel
import time
import random


@celery_app.task
def foo_task(name: str):
    time.sleep(random.randint(1, 20))
    user = UserModel(name=name)
    db.session.add(user)
    db.session.commit()
    return {"data": f"create user {name} success."}
