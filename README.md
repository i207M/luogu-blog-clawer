# Luogu Blog Clawer

爬取个人洛谷博客的Markdown源码。

受限制于洛谷博客不支持全文搜索，无奈，只好保存到本地进行搜索。

## Usage

1. 创建`params.py`文件，并参照`params_example.py`填写：
   - 请求头`headers`
   - 洛谷博客管理后台的最大页数`ADMIN_PAGE_MAX`
2. 运行`clawer.py`

`.md`文件会保存到`clawed`文件夹内，程序会产生临时文件`history.txt, swap.txt`。

## Attention

请勿滥用！如有疑问，请提出Issue或邮件联系。

---

欢迎Star~
