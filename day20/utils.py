# -*- coding:utf-8 -*-
from lxml import etree


class infoList(object):
    def __init__(self):
        file = open("01", "r")
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


p = infoList()
h = p.getHeaders()
print(h)
