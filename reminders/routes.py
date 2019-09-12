from flask import render_template, redirect, flash
from . import app
from .forms import ReminderForm


@app.route('/')
@app.route('/index')
def index():
    form = ReminderForm()
    reminders = [{'message': 'Do a thing', 'guid': '0000'}]
    return render_template('index.html', title='Home', reminders=reminders, form=form)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    reminders = [{'message': 'Do a thing', 'guid': '0000'}]
    return render_template('edit.html', title='Home', reminder=reminders[0], form=form)


@app.route('/save', methods=['GET', 'POST'])
def save():
    form = ReminderForm()
    flash("Saving reminder, maybe: {}".format(form.validate_on_submit()))
    if form.validate_on_submit():
        # Do a save
        flash("Saving reminder {}".format(form.message))
        return redirect('/index')
    reminders = [{'message': 'Do a thing', 'guid': '0000'}]
    return render_template('edit.html', title='Home', reminder=reminders[0], form=form)
