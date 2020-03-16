# -*-coding=utf-8-*-

# @Time : 2020/3/11 15:28
# @File : views.py
import datetime
import tushare as ts
from . import jingzhi
from flask import request,render_template,flash
from .forms import QueryJZ,UpdateJZ
from .function import cursor,con
GJ_BASE=1000

LABELS=['Date','Assert','Change','NetValue','NetValuePercent','Share','Profit','HS300']
HS_START=4138.51

@jingzhi.route('gj_info',methods=['GET','POST'])
def gj_info():

    update_form = UpdateJZ()
    query_form = QueryJZ()
    stock_type='GJ'
    if request.method=='GET':
        return render_template('jingzhi.html',query_form =query_form,update_form=update_form,stock_type=stock_type)

    else:

        if query_form.submit1.data and query_form.validate_on_submit():
            print('query_form')
            sql='select * from tb_jingzhi_gj_flask'
            cursor.execute(sql)
            ret=cursor.fetchall()
            content_list=[]
            for item in ret:
                date=item.get(LABELS[0]).strftime('%Y-%m-%d')
                Assert=int(item.get(LABELS[1]))
                Change=int(item.get(LABELS[2]))
                netvalue=item.get(LABELS[3])
                netvaluepercent=item.get(LABELS[4])
                share=int(item.get(LABELS[5]))
                profit=int(item.get(LABELS[6]))
                hs300=item.get(LABELS[7])
                content_list.append([date,Assert,Change,netvalue,netvaluepercent,share,profit,hs300])
            content_list=content_list[::-1]
            return render_template('jingzhi.html',stock_type=stock_type,query_form =query_form,update_form=update_form,labels=LABELS,content=content_list)

        elif update_form.submit2.data and update_form.validate_on_submit():
            df = ts.get_index()
            current_v = df[df['code'] == '000300']['close'].values[0]
            hs_latest = round(float(current_v) / HS_START, 2)

            change = update_form.change.data
            money=update_form.money.data
            # change 有正和负
            if change is None:

                change=0


            sql = 'select * from tb_jingzhi_gj_flask order by id desc limit 1'
            cursor.execute(sql)
            ret=cursor.fetchone()
            last_netvalue= ret.get('NetValue')
            last_assert= ret.get('Assert')
            share= ret.get('Share')

            change_share = int(change*last_netvalue)
            new_share = share+change_share
            latest_net = round(money/new_share,4)
            net_value_diff_p = round((latest_net-last_netvalue)/last_netvalue*100,2)
            new_profit=money-last_assert-change
            print(datetime.datetime.now(),money,change,last_netvalue,net_value_diff_p,new_share,new_profit,hs_latest)
            update_sql = 'insert into `tb_jingzhi_gj_flask` (`Date`,`Assert`,`Change`,`NetValue`,`NetValuePercent`,`Share`,`Profit`,`HS300`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(update_sql,(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),money,change,latest_net,net_value_diff_p,new_share,new_profit,hs_latest))
            try:
                con.commit()
            except Exception as e:
                print(e)
                con.rollback()
            else:
                print('update successfully')
                # con.close()
                # 使用flash提醒
                flash('update jz in db!')
            return render_template('jingzhi.html',stock_type=stock_type,query_form =query_form,update_form=update_form)

@jingzhi.route('hb_info',methods=['GET','POST'])
def hb_info():

    update_form = UpdateJZ()
    query_form = QueryJZ()
    stock_type='HB'
    if request.method=='GET':
        return render_template('jingzhi.html',query_form =query_form,update_form=update_form,stock_type=stock_type)

    else:

        if query_form.submit1.data and query_form.validate_on_submit():
            sql='select * from tb_jingzhi_hb_flask'
            cursor.execute(sql)
            ret=cursor.fetchall()
            content_list=[]
            for item in ret:
                date=item.get(LABELS[0]).strftime('%Y-%m-%d')
                Assert=int(item.get(LABELS[1]))
                Change=int(item.get(LABELS[2]))
                netvalue=item.get(LABELS[3])
                netvaluepercent=item.get(LABELS[4])
                share=int(item.get(LABELS[5]))
                profit=int(item.get(LABELS[6]))
                hs300=item.get(LABELS[7])
                content_list.append([date,Assert,Change,netvalue,netvaluepercent,share,profit,hs300])
            content_list=content_list[::-1]
            return render_template('jingzhi.html',stock_type=stock_type,query_form =query_form,update_form=update_form,labels=LABELS,content=content_list)

        elif update_form.submit2.data and update_form.validate_on_submit():
            df = ts.get_index()
            current_v = df[df['code'] == '000300']['close'].values[0]
            hs_latest = round(float(current_v) / HS_START, 2)

            change = update_form.change.data
            money=update_form.money.data
            # change 有正和负
            if change is None:

                change=0


            sql = 'select * from tb_jingzhi_hb_flask order by id desc limit 1'
            cursor.execute(sql)
            ret=cursor.fetchone()
            last_netvalue= ret.get('NetValue')
            last_assert= ret.get('Assert')
            share= ret.get('Share')

            change_share = int(change*last_netvalue)
            new_share = share+change_share
            latest_net = round(money/new_share,4)
            net_value_diff = latest_net-last_netvalue
            net_value_diff_p = round((latest_net-last_netvalue)/last_netvalue*100,2)
            new_profit=money-last_assert-change
            # print(datetime.datetime.now(),money,change,last_netvalue,net_value_diff_p,new_share,new_profit,hs_latest)
            update_sql = 'insert into `tb_jingzhi_hb_flask` (`Date`,`Assert`,`Change`,`NetValue`,`NetValuePercent`,`Share`,`Profit`,`HS300`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
            cursor.execute(update_sql,(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),money,change,latest_net,net_value_diff_p,new_share,new_profit,hs_latest))
            try:
                con.commit()
            except Exception as e:
                print(e)
                con.rollback()
            else:
                print('update successfully')
                # con.close()
                flash('update jz in db!')

            return render_template('jingzhi.html',stock_type=stock_type,query_form =query_form,update_form=update_form)
