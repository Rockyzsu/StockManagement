# -*-coding=utf-8-*-

# @Time : 2020/3/12 16:36
# @File : views.py
from flask import render_template
from .forms import RealTimeForm
from . import realtime

@realtime.route('real',methods=['GET','POST'])
def monitor():
    form = RealTimeForm()
    return render_template('realtime.html',form=RealTimeForm())

