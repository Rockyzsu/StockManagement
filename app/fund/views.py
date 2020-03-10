from . import fund
from flask import jsonify,render_template
from .forms import QueryFund
from .function import fetch
@fund.route('info',methods=['GET','POST'])
def fund_info():
    form = QueryFund()
    percent=''
    if form.validate_on_submit():
        code = form.code.data
        percent = fetch(code)

    return render_template('fund.html',form=form,percent=percent)


@fund.route('price')
def fund_price():
    return jsonify({'status':200,'msg':'Get fund price'})