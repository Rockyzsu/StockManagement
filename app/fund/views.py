from . import fund
from flask import jsonify,render_template
from .forms import QueryFund,QueryCB
from .function import fetch
@fund.route('fund',methods=['GET','POST'])
def fund_price():
    form = QueryFund()
    name,price,percent='','',''

    if form.search.data and form.validate_on_submit():
        code = form.code.data
        name,price,percent = fetch(code)

    return render_template('fund.html',form=form,price=price,name=name,percent=percent)


@fund.route('cb')
def cb_price():
    form = QueryCB()
    name,price,percent='','',''

    if form.search_bt.data and form.validate_on_submit():
        code = form.cb_code.data
        name,price,percent = fetch(code)
    return render_template('fund.html',form=form,price=price,name=name,percent=percent)

