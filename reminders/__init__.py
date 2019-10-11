from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
db = SQLAlchemy(app)

from .models import Reminder
from . import routes
from . import api

if app.env == 'development':
    print("Debug mode, creating DB and some reminders.")
    db.create_all()
    if len(Reminder.query.all()) == 0:
        reminder1 = Reminder(message='Do a thing.')
        reminder2 = Reminder(message='Do another thing.')
        db.session.add(reminder1)
        db.session.add(reminder2)
        db.session.commit()
if app.env == 'production':
    # Prod mode, just ensure DB exists.
    db.create_all()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Reminder': Reminder}
