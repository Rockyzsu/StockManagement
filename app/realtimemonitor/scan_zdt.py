def get_zg_code():
    '''
    获取正股代码
    '''
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
        zg_code = item.get('pre_bond_id').strip()[2:]

        b = []
        for i in range(len(a)):
            b.append(str(a[i][0]).lower())
        c = ''.join(b)
        result.setdefault(c,[])
        result[c].append({bond_id:bond_nm})

    return resultcb_code_fun():
    



