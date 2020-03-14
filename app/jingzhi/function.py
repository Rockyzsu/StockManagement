# -*-coding=utf-8-*-

# @Time : 2020/3/12 9:55
# @File : function.py
import pymysql
from config import DB_PASSWORD
con = pymysql.connect(host='127.0.0.1',port=3306,user='root',password=DB_PASSWORD,db='db_stock',cursorclass=pymysql.cursors.DictCursor)
cursor = con.cursor()
