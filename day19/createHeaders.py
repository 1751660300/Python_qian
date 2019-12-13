# -*- coding:gbk -*-
from lxml import etree


class infoList(object):
    def __init__(self):
        file = open("info.txt", "r")
        self.info = file.read()
        file.close()

    def getHeaders(self):
        hd = {}
        et = etree.HTML(self.info)
        head = et.xpath("//headers/text()")
        for i in head:
            k = i.split("\n")
            for j in k:
                l1 = j.split(": ")
                hd[l1[0].strip("\n")] = l1[1].strip("\n")
        return hd

    def getParams(self):
        pa = {}
        et = etree.HTML(self.info)
        head = et.xpath("//Params/text()")
        for i in head:
            l1 = i.split(": ")
            pa[l1[0].strip("\n")] = l1[1].strip("\n")
        return pa

    def getCookies(self):
        co = {}
        et = etree.HTML(self.info)
        head = et.xpath("//cookies/text()")
        for i in head:
            l1 = i.split(": ")
            co[l1[0].strip("\n")] = l1[1].strip("\n")
        return co
