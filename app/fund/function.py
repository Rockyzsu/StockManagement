import requests
url='http://qt.gtimg.cn/q={}'
session = requests.Session()

def fetch(code):

    r = session.get(
        url=url.format(code)
    )
    content_list = r.text.split('~')
    ret = content_list[3]
    return ret