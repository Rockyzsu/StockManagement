# -*-coding=utf-8-*-

# @Time : 2020/3/11 15:39
# @File : forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DecimalField,FloatField,BooleanField
from wtforms.validators import DataRequired,Length,Optional
class QueryFund(FlaskForm):

    search = SubmitField('search')

    jz = StringField('Today asset',validators=[Optional()])
    update = SubmitField('update')
