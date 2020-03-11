# -*-coding=utf-8-*-

# @Time : 2020/3/11 11:11
# @File : __init__.py.py
from flask import Blueprint

cb = Blueprint('cb',__name__)

from . import views
