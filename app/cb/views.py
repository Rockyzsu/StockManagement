# -*-coding=utf-8-*-

# @Time : 2020/3/11 11:11
# @File : views.py
from . import cb
from flask import render_template,request
from .function import jsl_fetch,zz_filter,zg_filter
from .forms import QueryFund

@cb.route('jsl',methods=['GET','POST'])
def jsl():
    labels = []
    content = [[]]
    form = QueryFund()

    if request.method=='GET':

        return render_template('jsl.html',labels=labels,content=content,form=form)

    else:
        if form.validate_on_submit():
            zg_condition = form.zg_condition.data
            zz_condition = form.zz_condition.data
            zg_num = form.zg_num.data
            zz_num = form.zz_num.data

            # print(zg_num,zz_num)
            # print(zg_condition,zz_condition,zg_num,zz_num)
            # False False None None 全为空的时候
            # num = form.num.data

            df = jsl_fetch()

            if df is None:

                return render_template('jsl.html', labels=labels, content=content,form=form)

            if zg_num is not None:
                op ='gt' if zg_condition else 'lt'
                df=zg_filter(df,zg_num,op)

            if zz_num is not None:
                op ='gt' if zz_condition else 'lt'
                df=zz_filter(df,zz_num,op)


            df=df[['bond_id', 'bond_nm', 'price',  'increase_rt','sincrease_rt','premium_rt']]
            labels = df.columns.values.tolist()
            content=df.values.tolist()
            total=len(content)
            return render_template('jsl.html',labels=labels,content=content,form=form,total=total)
