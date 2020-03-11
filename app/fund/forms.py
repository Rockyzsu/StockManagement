from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length
class QueryFund(FlaskForm):

    code = StringField('Code',validators=[DataRequired(),Length(6,8)])
    submit = SubmitField('Search')
