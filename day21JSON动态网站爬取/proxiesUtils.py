# -*- coding:utf-8 -*-
from lxml import etree
import requests
import retrying
from day21JSON动态网站爬取 import utils


@retrying.retry(stop_max_delay=200, stop_max_attempt_number=1)
def res(p, hd):
    re = requests.get("http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%99%BE%E5%BA%A6%E5%A4%B4%E5%83%8F&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E7%99%BE%E5%BA%A6%E5%A4%B4%E5%83%8F&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=30&rn=30&gsm=&1575974931806="
, headers=hd, proxies=p)
    return re.status_code


def getProxies():
    file = open("XiCi01.html", "r", encoding="utf-8")
    s = file.read()
    file.close()
    e = etree.HTML(s)
    ip_list = e.xpath('//td[2]/text()')
    dKou_list = e.xpath('//td[3]/text()')
    lXin_list = e.xpath('//td[6]/text()')
    i = 0
    data_list = []
    while i < len(lXin_list):
        print("{}:{}".format(i, len(lXin_list)))
        dic = {lXin_list[i].lower(): lXin_list[i].lower() + '://' + ip_list[i] + ':' + dKou_list[i]}
        try:
            info = utils.infoList()
            if res(dic, info.getHeaders()) == 200:
                print(dic)
                data_list.append(dic)
        except Exception as e:
            print(e)
        i += 1
    return data_list


# getProxies()

