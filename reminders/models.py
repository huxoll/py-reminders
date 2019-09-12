from . import db
from datetime import datetime
import uuid


def generate_uuid():
    return str(uuid.uuid4())


class TimestampMixin(object):
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime)


class Reminder(TimestampMixin, db.Model):
    guid = db.Column(db.String(48), primary_key=True, default=generate_uuid)
    message = db.Column(db.String(255))

    def __repr__(self):
        return '<Reminder {}>'.format(self.message)

