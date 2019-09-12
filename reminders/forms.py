from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class ReminderForm(FlaskForm):
    message = StringField('Message', validators=[DataRequired()])
    guid = HiddenField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Save')
