# -*-coding=utf-8-*-

# @Time : 2020/3/11 11:11
# @File : views.py
from . import cb
from flask import render_template,request,flash
from .function import jsl_fetch,zz_filter,zg_filter
from .forms import CBForm

@cb.route('list',methods=['GET','POST'])
def get_cb_list():
    labels = []
    content = [[]]
    form = CBForm()

    if request.method=='GET':

        return render_template('cb_list.html',labels=labels,content=content,form=form)

    else:
        if form.validate_on_submit():
            zg_condition = form.zg_condition.data
            zz_condition = form.zz_condition.data
            zg_num = form.zg_num.data
            zz_num = form.zz_num.data


            df = jsl_fetch()

            if df is None:

                return render_template('cb_list.html', labels=labels, content=content,form=form)

            if zg_num is not None:
                op ='gt' if zg_condition else 'lt'
                df=zg_filter(df,zg_num,op)

            if zz_num is not None:
                op ='gt' if zz_condition else 'lt'
                df=zz_filter(df,zz_num,op)

            df=df.sort_values(by='increase_rt',ascending=False)

            df=df[['bond_id', 'bond_nm', 'price',  'increase_rt','sincrease_rt','premium_rt']]
            labels = df.columns.values.tolist()
            content=df.values.tolist()
            total=len(content)
            flash('update suceessfully!')
            return render_template('cb_list.html',labels=labels,content=content,form=form,total=total)
