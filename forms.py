from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Regexp
from wtforms import StringField, SubmitField

class NumberForm(FlaskForm):
    number = StringField(validators=[
        DataRequired("Please type something into the box."), 
        Length(15, 19, message="The length of the number you provided is invalid."),
        Regexp(r' ^[0-9]*$', message='Please enter only numbers')])
    
    submit = SubmitField("Validate")
