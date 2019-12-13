# -*- coding:utf-8 -*-
import requests
from lxml import etree
from day19 import createHeaders


class Spider(object):
    def __init__(self):
        self.all_url = ["http://www.cssmoban.com/tags.asp?page={}&n=%E5%8D%9A%E5%AE%A2&sb=GO".format(i) for i in range(1, 23)]
        # print(self.all_url)

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
        }

    def run(self):
        img_list = []
        title_list = []
        info = createHeaders.infoList()
        for url in self.all_url:
            response = requests.get(url, headers=info.getHeaders())
            # 将响应对象转换成text或者element对象
            html = etree.HTML(response.text)
            img_list = html.xpath("//li/a/img/@src")
            title_list = html.xpath("//li/a/img/@alt")
            # print(img_list)
            # print(title_list)
            item = {}
            for index, img in enumerate(img_list):
                item["img"] = img
                item["title"] = title_list[index]
                print(item)


if __name__ == "__main__":
    Spider = Spider()
    Spider.run()
