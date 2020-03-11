# -*-coding=utf-8-*-

# @Time : 2020/3/11 15:27
# @File : __init__.py.py
from flask import Blueprint
jingzhi = Blueprint('jingzhi',__name__)
from . import views
