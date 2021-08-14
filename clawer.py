import time
import re
import codecs

import requests

from headers import headers

ADMIN_BASE = 'https://www.luogu.com.cn/blogAdmin/article/list?status=%5B1%2C2%5D&solution=%5B%5D&page={}&pageType=list&name=&status-check=1&status-check=2&order=0'

# ----------------MODIFY----------------
ADMIN_PAGE_MAX = 40
# ----------------MODIFY----------------


def process(url: str):
    ret = requests.get(url, headers=headers)
    title = ''
    for line in ret.text.splitlines():
        if line.startswith(
            '<input name="title" class="mdui-textfield-input" type="text" placeholder="标题" value="'
        ):
            title = line[85:-3]
        if line.startswith('        var articleContent = "'):
            post = line[30:-2]
            post = post.replace(r'\/', '/')
            post = codecs.decode(post, 'unicode_escape')
            open('clawed/' + title + '.md', 'w').write(post)
    if (title == ''):
        print(ret.text)
        raise
    print(f'Clawed {title}')


for admin_page in range(1, ADMIN_PAGE_MAX + 1):
    print(f'Admin Page #{admin_page}')
    ret = requests.get(ADMIN_BASE, headers=headers)
    url_list = re.findall(r'/blogAdmin/article/edit/\d+', ret.text)
    for url in url_list:
        time.sleep(10)
        process('https://www.luogu.com.cn' + url)
