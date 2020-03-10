from . import fund
from flask import jsonify

@fund.route('/price')
def fund_price():
    return jsonify({'status':200,'msg':'Get fund price'})