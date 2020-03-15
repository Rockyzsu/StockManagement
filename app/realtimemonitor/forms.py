from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DecimalField,FloatField,BooleanField
from wtforms.validators import DataRequired,Length,Optional


class RealTimeForm(FlaskForm):

    submit = SubmitField('start Monitor')
    stop=SubmitField('Stop monitor')