import codecs
import html
import os
import re
import time

import requests

from params import headers, ADMIN_PAGE_MAX

ADMIN_BASE = 'https://www.luogu.com.cn/blogAdmin/article/list?status=%5B1%2C2%5D&solution=%5B%5D&page={}&pageType=list&name=&status-check=1&status-check=2&order=0'
INTERVAL = 10


def process(url: str):
    url = 'https://www.luogu.com.cn' + url

    ret = requests.get(url, headers=headers)
    ret = ret.content.decode('utf-8')
    filename = ''
    for line in ret.splitlines():
        if line.startswith(
            '<input name="title" class="mdui-textfield-input" type="text" placeholder="标题" value="'
        ):
            title = line[85:-3]
            filename = html.unescape(title)
            filename = re.sub(r'[^\w_.)( -]', '_', filename)
            if title != filename:
                open('swap.txt', 'a+', encoding='utf=8').write(f'{title} => {filename}\n')
        if line.startswith('        var articleContent = "'):
            post = line[30:-2]
            post = post.replace(r'\/', '/')
            post = codecs.decode(post, 'unicode_escape')
            open('clawed/' + filename + '.md', 'w', encoding='utf-8').write(post)

    if (filename == ''):
        raise Exception('TitleNotFound')
    print(f'Clawed {filename}')


# if __name__ == '__main__':
#     process('/blogAdmin/article/edit/142252')
#     exit(0)

if __name__ == '__main__':
    history_set = set(open('history.txt').read().splitlines()
                      ) if os.path.exists('history.txt') else set()
    os.makedirs('clawed', exist_ok=True)

    for admin_page in range(1, ADMIN_PAGE_MAX + 1):
        time.sleep(INTERVAL)
        print(f'Admin Page #{admin_page}')
        ret = requests.get(ADMIN_BASE.format(admin_page), headers=headers)
        url_list = re.findall(r'/blogAdmin/article/edit/\d+', ret.text)

        for url in url_list:
            if url in history_set:
                continue
            time.sleep(INTERVAL)
            try:
                process(url)
            except Exception as e:
                print(f'WRONG: {url}')
                print(e)
            else:
                open('history.txt', 'a+').write(url + '\n')
