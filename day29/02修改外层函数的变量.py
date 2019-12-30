# -*- coding:utf-8 -*-
def out(a, b):  # 外层函数
    def inner(c):  # 内层函数
        nonlocal a, b
        print(a, b, c, a + b + c)
        a = a + 1
        b = b * 2
        print(a, b, c, a+b+c)
    return inner  # 返回内层函数的地址


o = out(1, 2)
o(1)