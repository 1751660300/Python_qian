# -*- coding:utf-8 -*-
from lxml import etree
import requests
from day19 import createHeaders


class dou(object):
    def __init__(self, url):
        self.info = createHeaders.infoList()
        self.url = url

    def getData(self, str1):
        dataList = []
        for url in self.url:
            response = requests.get(url, headers=self.info.getHeaders())
            html = etree.HTML(response.text)
            data = html.xpath(str1)
            dataList.extend(data)
        return dataList


# url_list = ["http://www.cssmoban.com/tags.asp?page={}&n=css3".format(i) for i in range(1, 23)]
url_list = ["http://www.cssmoban.com/tags.asp?page={}&n=css3".format(i) for i in range(1, 23)]
data = dou(url_list)
img = data.getData("//img[@class=\"thumbImgs\"]/@src")
title = data.getData("//img[@class=\"thumbImgs\"]/@alt")
i = 0
while i < len(img):
    print(title[i], img[i], sep=":")
    i += 1


