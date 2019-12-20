# -*- coding:utf-8 -*-
from lxml import etree
import random


class infoList(object):
    def __init__(self):
        # file = open('F:\pycharm\Python_qian\myUtils\headInfo', "r", encoding="utf-8")
        file = open('/root/PycharmProjects/Python_qian/myUtils/headInfo', "r", encoding="utf-8")
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
        head = self.et.xpath("//params/text()")
        for i in head:
            l1 = i.split(": ")
            pa[l1[0]] = l1[1]
        return pa


# p = infoList()
# h = p.getHeaders()
# print(h)
