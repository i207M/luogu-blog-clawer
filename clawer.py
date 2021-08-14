import re

import requests

from headers import headers

ADMIN_BASE = 'https://www.luogu.com.cn/blogAdmin/article/list?status=%5B1%2C2%5D&solution=%5B%5D&page={}&pageType=list&name=&status-check=1&status-check=2&order=0'
RE_STR = r'/blogAdmin/article/edit/\d+'

# ----------------MODIFY----------------
ADMIN_PAGE_MAX = 40
# ----------------MODIFY----------------


def process():
    pass


for admin_page in range(1, ADMIN_PAGE_MAX + 1):
    ret = requests.get(ADMIN_BASE, headers=headers)
    url_list = re.findall(RE_STR, ret.text)
    for url in url_list:
        process('https://www.luogu.com.cn' + url)
