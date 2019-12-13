from lxml import etree
import requests
from day19 import createHeaders


class dou(object):
    def __init__(self, url):
        self.info = createHeaders.infoList()
        print(self.info.getHeaders())
        self.url = url

    def getData(self, str1):
        dataList = []
        for url in self.url:
            response = requests.get(url, headers=self.info.getHeaders())
            html = etree.HTML(response.text)
            data = html.xpath(str1)
            dataList.extend(data)
        return dataList


url_list = ["https://movie.douban.com/top250?start=" + str(i) for i in range(0, 256, 25)]
d = dou(url_list)
img = d.getData("//img[@width=\"100\"]/@src")
title = d.getData("//span[@class=\"title\"][1]/text()")
inq = d.getData("//span[@class=\"inq\"]/text()")
i = 0
dc = []
while i < len(img):
    d = {"img": img[i], "title": title[i], "inq": inq[i]}
    dc.append(d)
    i += 1
for i in dc:
    print(i)
