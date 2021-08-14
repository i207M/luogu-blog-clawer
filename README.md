# Luogu Blog Clawer

爬取个人洛谷博客的Markdown源码。

受限制于洛谷博客不支持全文搜索，无奈，只好保存到本地进行搜索。

## Usage

1. 创建`headers.py`文件，以`dict`的形式保存所有请求头。以下是示例文件：

```
headers = {
    'authority': 'www.luogu.com.cn',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': '',
    'accept': '',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': '',
    'cookie': '',
}
```

2. 打开`clawer.py`，修改`ADMIN_PAGE_MAX`为管理后台的最大页数。

3. 运行`clawer.py`

## Attention

请勿滥用！如有疑问，请提出Issue或邮件联系。

---

欢迎Star~
