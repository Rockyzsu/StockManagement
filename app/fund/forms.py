from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import Required
class QueryFund(FlaskForm):

    code = StringField('Code',validators=[Required()])
    submit = SubmitField('Search')
