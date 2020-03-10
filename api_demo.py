# -*-coding=utf-8-*-

# @Time : 2020/3/4 13:48
# @File : api_demo.py
import requests
url='http://127.0.0.1:6789/{}'
code=''
requests.get(url.format('fund_price'),json={'code':code})
