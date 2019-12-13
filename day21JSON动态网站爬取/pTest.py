# -*- coding:utf-8 -*-
import requests
from day21JSON动态网站爬取 import utils
head = utils.infoList().getProxies()
for i in head:
    res = requests.get("https://www,baidu.com", proxies=i)
    if res.status_code != 200:
        print(i)

