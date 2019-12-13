# -*- coding:utf-8 -*-
from lxml import etree
import json
import jsonpath
from bs4 import BeautifulSoup


def writeData(path, data, geShi="w"):
    file = open(path, geShi)
    file.write(data)
    file.close()


def readData(path, geShi, encoding="utf-8"):
    file = open(path, geShi, encoding=encoding)
    data = file.read()
    file.close()
    return data


def lXmlExtract(express, data):
    e = etree.HTML(data)
    return e.xpath(express)


def jSonExtract(express, data):
    data_ = json.loads(data)
    # print(data)
    data_list = jsonpath.jsonpath(data_, express)
    return data_list


def bsExtractByFind(data, express, way):
    # boss 大唐 猪八戒 智联
    # data 需要提取的数据
    # way 借助"lxml",'parse','re'
    # express 表达式
    soup = BeautifulSoup(data, way)
    return soup.find(express)


def bsExtractByFind_all(data, express, way):
    soup = BeautifulSoup(data, way)
    return soup.find_all(express)


def bsExtractBySelect(data, express, way):
    soup = BeautifulSoup(data, way)
    return soup.select(express)


def bsExtractBySelec_one(data, express, way):
    soup = BeautifulSoup(data, way)
    return soup.select_one(express)