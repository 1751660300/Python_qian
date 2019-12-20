# -*- coding:utf-8 -*-
from lxml import etree
import random


class infoList(object):
    def __init__(self):
        # file = open("01", "r", encoding="utf-8")
        file = open("/root/PycharmProjects/Python_qian/多线程spider/01", "r", encoding="utf-8")
        self.et = etree.HTML(file.read())
        file.close()

    def getHeaders(self):
        hd = {}
        head = self.et.xpath("//headers/text()")[0].split("\n")
        for j in head:
            l1 = j.split(": ")
            hd[l1[0]] = l1[1]
        return hd

    def getParams(self):
        pa = {}
        head = self.et.xpath("//Params/text()")
        for i in head:
            l1 = i.split(": ")
            pa[l1[0]] = l1[1]
        return pa

    def getCookies(self):
        co = {}
        head = self.et.xpath("//cookies/text()")
        for i in head:
            l1 = i.split(": ")
            co[l1[0]] = l1[1]
        return co

    def getProxies(self):
        co = []
        head = self.et.xpath("//proxies/text()")
        for i in head:
            l1 = i.split("\t")
            dc = {l1[4]: l1[0] + ":" + l1[1]}
            co.append(dc)
        # return co[random.randint(1,len(co))]
        return co

# p = infoList()
# h = p.getProxies()
# print(h)
