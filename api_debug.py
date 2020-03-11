# -*-coding=utf-8-*-

# @Time : 2020/3/11 9:44
# @File : api_debug.py
from app.fund.function import fetch
from app.cb.function import jsl_fetch,zg_filter,zz_filter
# fetch('sz160216')
df=jsl_fetch()
# df=zz_filter(df,5,'gt')
df=zg_filter(df,7,'gt')
# print(df[['bond_id','bond_nm','price','sincrease_rt','increase_rt']])
print(df.colums_name)
