from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import Visitor, Host


class Visitor_CheckIn_Form(FlaskForm):
    visitor_name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    ph_number = IntegerField('Phone Number', validators=[DataRequired()]) 
    submit = SubmitField('Check-in')


class Visitor_CheckOut_Form(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    ph_number = IntegerField('Phone Number', validators=[DataRequired()]) 
    submit = SubmitField('Check-Out')


class HostForm(FlaskForm):
    host_name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    ph_number = IntegerField('Phone Number', validators=[DataRequired()]) 
    submit = SubmitField('Register')