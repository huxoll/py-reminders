from flask_restful import Resource, Api
from flask import jsonify
from flask import request
from flask import abort
from . import app, db
from .models import Reminder
from datetime import datetime

api = Api(app)


class ReminderListResource(Resource):
    def get(self):
        reminders = Reminder.query.filter_by(deleted_at=None)
        return jsonify([i.serialize for i in reminders.all()])

    def post(self):
        if not request.json or 'message' not in request.json:
            print("Got malformed json: ", request.json)
            abort(400)

        # reminder = Reminder.query.get(form.guid.data)
        reminder = Reminder()
        reminder.message = request.json['message']
        db.session.add(reminder)
        db.session.commit()
        return reminder.serialize, 201


class ReminderResource(Resource):
    def get(self, reminder_id):
        reminder = Reminder.query.get(reminder_id)
        return reminder.serialize, 200

    def put(self, reminder_id):
        if not request.json or 'message' not in request.json:
            print("Got malformed json: ", request.json)
            abort(400)
        reminder = Reminder.query.get(reminder_id)
        reminder.message = request.json['message']
        return reminder.serialize, 200

    def delete(self, reminder_id):
        reminder = Reminder.query.get(reminder_id)
        reminder.deleted_at = datetime.utcnow()
        db.session.add(reminder)
        db.session.commit()
        return 204


api.add_resource(ReminderListResource, '/api/reminders')
api.add_resource(ReminderResource, '/api/reminders/<string:reminder_id>')
