from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class ReminderForm(FlaskForm):
    message = StringField('Message', validators=[DataRequired()])
    guid = HiddenField('Guid')
    updated_at = HiddenField('Deleted At')
    deleted_at = HiddenField('Updated At')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Save')


class ReminderDeleteForm(FlaskForm):
    message = StringField('Message')
    guid = HiddenField('Guid', validators=[DataRequired()])
    submit = SubmitField('Delete')
