# -*- coding:utf-8 -*-
def out(a, b):  # 外层函数
    def inner():  # 内层函数
        print(a, b, a+b)
    return inner  # 返回内层函数的地址


o = out(1, 2)
o()





