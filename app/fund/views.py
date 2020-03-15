import json

from . import fund
from flask import jsonify, render_template,flash
from .forms import QueryFund, QueryCB, UpdateCBCode
from .function import fetch,update_cb_code_fun
import tushare as ts

try:
    conn = ts.get_apis()
except Exception as e:
    conn = None


# TODO mapping code and name as dict
try:
    f=open('codes.cfg','r')
    code_dict = json.load(f)
except Exception as e:

    code_dict=None

@fund.route('fund', methods=['GET', 'POST'])
def fund_info():
    form_fund = QueryFund()
    form_cb = QueryCB()
    form_update_cb_code = UpdateCBCode()

    if form_fund.search.data and form_fund.validate_on_submit():

        code = form_fund.code.data
        name, price, percent = fetch(code)
        return render_template('fund.html',
                               form_fund=form_fund,
                               form_cb=form_cb,
                               form_update_cb_code=form_update_cb_code,

                               price=price,
                               name=name,
                               percent=percent)

    elif form_cb.search_bt1.data and form_cb.validate_on_submit():
        text = form_cb.cb_code.data
        bond_id_list = code_dict.get(text)
        bond_name_dict = {}

        if text.isdigit():
            bond_list=[text]
            for item in bond_list:
                k=list(item.keys())[0]
                bond_list.append(k)
                v = list(item.values())[0]
                bond_name_dict[k]=v
        else:
            # pinyin
            if bond_id_list is None:
                flash('No dict found!')
                return render_template('fund.html',
                                       form_fund=form_fund,
                                       form_cb=form_cb,
                                       form_update_cb_code=form_update_cb_code,
                                       cb_percent='',
                                       cb_price='',
                                       ask1='',
                                       bid1='',
                                       diff=''
                                       )
            bond_list=[]
            for item in bond_id_list:
                k=list(item.keys())[0]
                bond_list.append(k)
                v = list(item.values())[0]
                bond_name_dict[k]=v
        try:
            df = ts.quotes(bond_list, conn=conn)
        except Exception as e:
            print(e)
            return render_template('fund.html',
                                   form_fund=form_fund,
                                   form_cb=form_cb,
                                   form_update_cb_code=form_update_cb_code,
                                   cb_percent='',
                                   cb_price='',
                                   ask1='',
                                   bid1='',
                                   diff=''
                                   )
        result_list=[]
        for index,row in df.iterrows():
            last_close = row['last_close'] / 10
            cb_price = round(row['price'] / 10, 1)
            cb_percent = round((cb_price - last_close) / last_close * 100, 1)
            ask1 = row['ask1']
            bid1 = row['bid1']
            diff = round((ask1 - bid1) / bid1 * 100, 1)
            d={}
            d['cb_price']=cb_price
            d['cb_percent']=cb_percent
            d['ask1']=round(ask1/10,1)
            d['bid1']=round(bid1/10,1)
            d['diff']=diff
            d['bond_name']=bond_name_dict.get(row['code']).replace('转债','')
            result_list.append(d)
        return render_template('fund.html',
                               form_fund=form_fund,
                               form_cb=form_cb,
                               form_update_cb_code=form_update_cb_code,
                               bond_lists=result_list
                               )
    elif form_update_cb_code.update_bt.data and form_update_cb_code.validate_on_submit():
            # 更新代码
            result = update_cb_code_fun()
            print('updating coding')
            with open('codes.cfg','w') as f:
                json.dump(result,f,ensure_ascii=False)
            flash('Update code succussfully!')
            return render_template('fund.html',
                                   form_fund=form_fund,
                                   form_cb=form_cb,
                                   form_update_cb_code=form_update_cb_code,
                                   )


    else:
        return render_template('fund.html',
                               form_fund=form_fund,
                               form_cb=form_cb,
                               form_update_cb_code=form_update_cb_code
                               )
