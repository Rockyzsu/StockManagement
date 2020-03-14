# -*-coding=utf-8-*-

# @Time : 2020/3/12 16:35
# @File : __init__.py.py
from flask import Blueprint
realtime = Blueprint('realtime',__name__)

from . import views
