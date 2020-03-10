# -*-coding=utf-8-*-

# @Time : 2020/3/4 13:42
# @File : server.py
from flask import Flask
from module.fund import Fund

app = Flask(__name__)
app.register_blueprint(Fund, url_prefix='')

if __name__=='__main__':
    app.run(port=PORT)
