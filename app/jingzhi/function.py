# -*-coding=utf-8-*-

# @Time : 2020/3/12 9:55
# @File : function.py
import pymysql
from config import DB_PASSWORD,DB_HOST,DB_PORT,DB_USER
con = pymysql.connect(host=DB_HOST,port=DB_PORT,user=DB_USER,password=DB_PASSWORD,db='db_stock',cursorclass=pymysql.cursors.DictCursor)
cursor = con.cursor()
