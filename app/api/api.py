from flask import Blueprint
from flask import jsonify
from app.celery.tasks import foo_task
from app.models import UserModel
from app.extensions import db
import uuid
from celery.result import AsyncResult
from app.celery import celery as celery_app

app = Blueprint("app", __name__)


@app.route("/")
def test():
    result = db.session.query(UserModel).count()
    name = uuid.uuid4().hex
    task = foo_task.delay(name)
    return jsonify({"task_id": task.id, "name": name, "total_user": result})


@app.route("/get/<task_id>", methods=["GET"])
def get_task_result(task_id):
    res = AsyncResult(task_id, app=celery_app)
    return res.state
