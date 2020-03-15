from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length,Optional
class QueryFund(FlaskForm):
    code = StringField('Fund info',validators=[DataRequired(),Length(6,10)])
    search = SubmitField('search')


class QueryCB(FlaskForm):
    cb_code = StringField('CB info',validators=[DataRequired()])
    search_bt1 = SubmitField('search')


class UpdateCBCode(FlaskForm):
    update_bt = SubmitField('Update code')
