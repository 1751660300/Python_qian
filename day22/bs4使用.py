# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

file = open("F:\pycharm\Python_qian\myUtils\XiCi01.html", "r", encoding="utf-8")
data = file.read()
file.close()
b = BeautifulSoup(data, "lxml")
list = b.select(".false")
print(b.prettify())
