# -*- coding:utf-8 -*-
import requests
import day20.utils
from lxml import etree


class Ppt(object):
    def __init__(self, url_list):
        self.url_list = url_list
        self.info = day20.utils.infoList()

    def getData(self, str1):
        data = []
        for i in self.url_list:
            res = requests.get(i, headers=self.info.getHeaders())
            e = etree.HTML(res.content)
            data.extend(e.xpath(str1))
            print("============获取数据成功============")
        return data


url = ["http://www.1ppt.com/xiazai/jianli/ppt_jianli_{}.html".format(i) for i in range(1, 7)]

title_str = "//h2/a[@target=\"_blank\"]/text()"
down_url_str = "//ul/li/a[@target=\"_blank\"]/@href"

ppt = Ppt(url)

data_list = ppt.getData(title_str)
data_url_list = ["http://www.1ppt.com/{}".format(i) for i in ppt.getData(down_url_str)]

down_ppt = Ppt(data_url_list)
real_url = down_ppt.getData("//ul[@class=\"downurllist\"]/li/a/@href")
print("============开始解析数据============")
di = dict(zip(data_list, real_url))
for i, j in di.items():
    print(i, j, sep=":")
