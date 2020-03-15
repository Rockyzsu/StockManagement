import requests
import pypinyin

url = 'http://qt.gtimg.cn/q={}'
session = requests.Session()
headers = {'User-Agent': 'FireFox Chrome Molliza Android Iphone'}
max_time = 2


def fetch(code):
    if len(code) == 6:
        if code.startswith('1'):
            code = 'sz' + code
        elif code.startswith('5'):
            code = 'sh' + code
        else:
            print('代码异常')
            return None,None,None
    retry = 0
    while retry < max_time:
        try:
            r = session.get(
                url=url.format(code),
                headers=headers,
                timeout=3
                )
        except Exception as e:
            print(e)
            retry += 1
        else:
            break

    if retry == max_time:
        print(url.format(code))
        return None,None,None

    content_list = r.text.split('~')

    name = content_list[1]
    price = content_list[3]
    percent = content_list[32]
    return name, price,percent

def update_cb_code_fun():
    cookies = {
        'auto_reload': 'true',
        'kbzw_r_uname': '%E9%87%8F%E5%8C%96%E8%87%AA%E7%94%B1%E4%B9%8B%E8%B7%AF',
        'kbz_newcookie': '1',
        'kbzw__Session': '1kmak8h8v6pscf5brjllb9hfk3',
        'Hm_lvt_164fe01b1433a19b507595a43bf58262': '1578275141,1578879529',
        'Hm_lpvt_164fe01b1433a19b507595a43bf58262': '1579488732',
    }

    headers = {
        'Origin': 'https://www.jisilu.cn',
        'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.jisilu.cn/data/cbnew/',
        'Sec-Fetch-Site': 'same-origin',
    }


    data = {
      'fprice': '',
      'tprice': '',
      'volume': '',
      'svolume': '',
      'premium_rt': '',
      'ytm_rt': '',
      'rating_cd': '',
      'is_search': 'Y',
      'btype': 'C',
      'listed': 'Y',
      'sw_cd': '',
      'bond_ids': '',
      'rp': '50'
    }


    try:
        response = session.post('https://www.jisilu.cn/data/cbnew/cb_list/', headers=headers, params={}, cookies=cookies, data=data,timeout=3)
    except Exception as e:
        print(e)
        return None

    ret = response.json()
    result = {}
    for body_dict in ret.get('rows',[]):
        # print(item)

        item=body_dict.get('cell',{})
        bond_nm = item.get('bond_nm','').strip()
        bond_id = item.get('bond_id','').strip()
        a=pypinyin.pinyin(bond_nm, style=pypinyin.FIRST_LETTER)

        b = []
        for i in range(len(a)):
            b.append(str(a[i][0]).lower())
        c = ''.join(b)
        result.setdefault(c,[])
        result[c].append({bond_id:bond_nm})

    return result



if __name__=='__main__':
    print(update_cb_code_fun())