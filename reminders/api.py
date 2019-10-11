from flask_restful import Resource, Api
from flask import jsonify
from . import app, db
from .models import Reminder

api = Api(app)

class ReminderListResource(Resource):
    def get(self):
        reminders = Reminder.query.filter_by(deleted_at=None)
        return jsonify([i.serialize for i in reminders.all()])

    def post(self):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}, 201

class ReminderResource(Resource):
    def get(self, reminder_id):
        return {todo_id: todos[todo_id]}

    def put(self, reminder_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(ReminderListResource, '/api/reminders')
api.add_resource(ReminderResource, '/api/reminders/<string:todo_id>')

