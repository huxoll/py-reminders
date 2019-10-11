from . import db
from datetime import datetime
import uuid

def generate_uuid():
    return str(uuid.uuid4())

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%d %H:%M:%S")

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

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'guid' : self.guid,
           'message' : self.message,
           'created_at': dump_datetime(self.created_at),
           'updated_at': dump_datetime(self.updated_at),
           'deleted_at': dump_datetime(self.deleted_at)
       }
