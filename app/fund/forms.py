from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length,Optional
class QueryFund(FlaskForm):
    code = StringField('input code',validators=[DataRequired(),Length(6,10)])
    search = SubmitField('search')


class QueryCB(FlaskForm):
    cb_code = StringField('input code',validators=[DataRequired(),Length(6,10)])
    search_bt = SubmitField('search')
