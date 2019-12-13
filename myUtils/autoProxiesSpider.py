# -*- coding:utf-8 -*-
import time
import random
import requests
from day21JSON动态网站爬取 import utils


def st(queue, url_list):
    proxies_list = []
    data_list = []
    info = utils.infoList()
    i = 0
    while True:
        if i == len(url_list):
            break
        while True:
            if queue.empty():
                break
            dic = queue.get()
            proxies_list.append(dic)
        if len(proxies_list) > 5:
            res = requests.get(url_list[i], headers=info.getHeaders(),
                               proxies=proxies_list[random.randint(0, len(proxies_list))])
            data_list.append(res.content.decode("utf-8"))
            print("第{}次获取数据成功".format(i))
        else:
            time.sleep(0.5)
        i += 1
