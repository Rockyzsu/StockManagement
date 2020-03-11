# -*-coding=utf-8-*-

# @Time : 2020/3/11 14:00
# @File : forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DecimalField,FloatField,BooleanField
from wtforms.validators import DataRequired,Length,Optional
class QueryFund(FlaskForm):

    # zz_condition = BooleanField('zz勾选为大于',validators=[Optional()])
    # zz_num = FloatField('zz percent',validators=[Optional()])
    #
    # zg_condition = BooleanField('zg勾选为大于',validators=[Optional()])
    # zg_num = FloatField('zg percent',validators=[Optional()])


    zz_condition = BooleanField('zz勾选为大于',validators=[Optional()])
    zz_num = FloatField('zz percent',validators=[Optional()])

    zg_condition = BooleanField('zg勾选为大于',validators=[Optional()])
    zg_num = FloatField('zg percent',validators=[Optional()])


    submit = SubmitField('update')
