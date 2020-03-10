# -*-coding=utf-8-*-

# @Time : 2020/3/4 13:43
# @File : fund.py

from flask import Blueprint, request, jsonify
Fund = Blueprint('fund',__name__)

@Fund.route('/fund_price',methods=['POST'])
def fund_price():
    msg={'status':True}
    return jsonify(msg)
