import requests

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
