# -*-coding=utf-8-*-

# @Time : 2020/3/11 15:28
# @File : views.py
from . import jingzhi
from flask import request,render_template
from .forms import QueryFund

@jingzhi.route('info',methods=['GET','POST'])
def info():
    form = QueryFund()

    if request.method=='GET':
        return render_template('jingzhi.html',form=form)
    else:
        return render_template('jingzhi.html',form=form)
