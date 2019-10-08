from flask import render_template, redirect, flash
from . import app, db
from .forms import ReminderForm, ReminderDeleteForm
from .models import Reminder
from datetime import datetime


@app.route('/')
@app.route('/index')
def index():
    form = ReminderForm()
    reminders = Reminder.query.filter_by(deleted_at=None)

    return render_template('index.html', reminders=reminders,
                           form=form)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = ReminderForm()
    if form.guid.data:
        reminder = Reminder.query.get(form.guid.data)
        form.message.data = reminder.message
    return render_template('edit.html',
                           form=form)


@app.route('/save', methods=['GET', 'POST'])
def save():
    form = ReminderForm()
    reminder = None
    if form.validate_on_submit():
        # Do a save
        flash("Saved reminder \"{}\"".format(form.message.data))
        if form.guid.data:
            reminder = Reminder.query.get(form.guid.data)
        else:
            reminder = Reminder()
        reminder.message = form.message.data
        db.session.add(reminder)
        db.session.commit()
        return redirect('/index')
    if form.guid.data:
        reminder = Reminder.query.get(form.guid.data)
        form.message.data = reminder.message
    if reminder:
        return render_template('edit.html', reminder=reminder,
                               form=form)
    else:
        return render_template('edit.html', form=form)


@app.route('/delete', methods=['POST'])
def delete():
    form = ReminderDeleteForm()
    if form.validate_on_submit():
        if form.guid.data:
            reminder = Reminder.query.get(form.guid.data)
        else:
            return redirect('/index')
        # Do a delete
        reminder.deleted_at = datetime.utcnow()
        db.session.add(reminder)
        db.session.commit()
        flash("Deleted reminder \"{}\"".format(reminder.message))
        return redirect('/index')
        form.message.errors
    flash("Deleted reminder form guid \"{}\"".format(form.guid))
    flash("Deleted reminder error \"{}\"".format(form.errors))
    print("Form was not valid.")
    return render_template('edit.html',
                           form=form)
