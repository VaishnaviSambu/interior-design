from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class DesignRequestForm(FlaskForm):
    customer_name = StringField('Name', validators=[DataRequired()])
    customer_email = StringField('Email', validators=[DataRequired(), Email()])
    room_type = SelectField('Room Type', choices=[('living_room', 'Living Room'), ('bedroom', 'Bedroom'), ('kitchen', 'Kitchen')], validators=[DataRequired()])
    style_preference = SelectField('Style Preference', choices=[('modern', 'Modern'), ('classic', 'Classic'), ('industrial', 'Industrial')], validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')
