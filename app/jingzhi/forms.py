# -*-coding=utf-8-*-

# @Time : 2020/3/11 15:39
# @File : forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DecimalField,FloatField,BooleanField
from wtforms.validators import DataRequired,Length,Optional

class QueryJZ(FlaskForm):

    submit1 = SubmitField('show jz')

class UpdateJZ(FlaskForm):

    money = FloatField('money',validators=[DataRequired()])
    change = FloatField('change',validators=[Optional()])
    submit2 = SubmitField('update')
