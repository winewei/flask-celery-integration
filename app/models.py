from app.extensions import db
import sqlalchemy as sa
import datetime


class UserModel(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))
    create_at = sa.Column(sa.DateTime, default=datetime.datetime.utcnow)
