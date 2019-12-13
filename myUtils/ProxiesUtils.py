# -*- coding:utf-8 -*-
from lxml import etree
import requests
import retrying
from day21JSON动态网站爬取 import utils


@retrying.retry(stop_max_delay=200, stop_max_attempt_number=1)
def res(p, hd, url):
    # url 待爬的网站
    re = requests.get(url, headers=hd, proxies=p)
    return re.status_code


def getProxies(queue, url):
    file = open('F:\pycharm\Python_qian\myUtils\XiCi01.html', "r", encoding="utf-8")
    s = file.read()
    file.close()
    e = etree.HTML(s)
    ip_list = e.xpath('//td[2]/text()')
    dKou_list = e.xpath('//td[3]/text()')
    lXin_list = e.xpath('//td[6]/text()')
    i = 0
    while i < len(ip_list):
        print("{}:{}".format(i, len(lXin_list)))
        dic = {lXin_list[i].lower(): lXin_list[i].lower() + '://' + ip_list[i] + ':' + dKou_list[i]}
        try:
            info = utils.infoList()
            if res(dic, info.getHeaders(), url) == 200:
                # print(dic)
                queue.put(dic)
        except Exception as e:
            print(e)
        i += 1
