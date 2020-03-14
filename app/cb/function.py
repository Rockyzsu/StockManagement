# -*-coding=utf-8-*-

# @Time : 2020/3/11 11:15
# @File : function.py
import time
import pandas as pd
import requests

session = requests.Session()
headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
max_time = 2
post_data = {
    'btype': 'C',
    'listed': 'Y',
    'rp': '50',
    'is_search': 'Y'}

def convert_percent(x):
    try:
        ret = float(x) * 100
    except:
        ret = None
    return ret


def remove_percent(x):
    try:
        ret = x.replace(r'%', '')
        ret = float(ret)
    except Exception as e:
        ret = None

    return ret

def convert_float(x):
    try:
        ret_float = float(x)
    except:
        ret_float = None
    return ret_float

def remove_name(x):
    try:
        x=x.replace('转债','')
    except:
        pass
    return x

def jsl_fetch():
    timestamp = int(time.time() * 1000)
    url = 'https://www.jisilu.cn/data/cbnew/cb_list/?___jsl=LST___t={}'.format(timestamp)

    retry = 0

    while retry < max_time:

        try:
            r = session.post(
                url=url,
                headers=headers,
                data=post_data,
                timeout=3)

        except Exception as e:
            print(e)
            retry += 1
        else:
            break

    if retry == max_time:
        return None

    if not r:
        return None

    ret = r.json()
    bond_list = ret.get('rows', {})
    cell_list = []
    for item in bond_list:
        cell_list.append(pd.Series(item.get('cell')))
    df = pd.DataFrame(cell_list)
    # print(df)

    df['premium_rt'] = df['premium_rt'].map(lambda x: float(x.replace('%', '')))
    df['price'] = df['price'].astype('float64')
    df['convert_price'] = df['convert_price'].astype('float64')
    df['premium_rt'] = df['premium_rt'].astype('float64')
    df['redeem_price'] = df['redeem_price'].astype('float64')

    df['put_convert_price'] = df['put_convert_price'].map(convert_float)
    df['sprice'] = df['sprice'].map(convert_float)
    df['ration'] = df['ration'].map(convert_percent)
    df['volume'] = df['volume'].map(convert_float)
    df['convert_amt_ratio'] = df['convert_amt_ratio'].map(remove_percent)
    df['ration_rt'] = df['ration_rt'].map(convert_float)
    df['increase_rt'] = df['increase_rt'].map(remove_percent)
    df['sincrease_rt'] = df['sincrease_rt'].map(remove_percent)
    df['bond_nm'] = df['bond_nm'].map(remove_name)

    return df

def zg_filter(df,percent,operator):
    if operator=='gt':
        df = df[df['sincrease_rt']>=percent]
    elif operator=='lt':
        df = df[df['sincrease_rt']<=percent]
    else:
        pass

    return df



def zz_filter(df,percent,operator):
    if operator=='gt':
        df = df[df['increase_rt']>=percent]
    elif operator=='lt':
        df = df[df['increase_rt']<=percent]
    else:
        pass

    return df
