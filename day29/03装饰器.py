# -*- coding:utf-8 -*-
import retrying


def out2(f):  # 外层函数
    def inner():  # 内层函数
        print("我是two")
        f_ = f()
        print("添加功能2")
        return f_

    return inner  # 返回内层函数的地址


def out1(f):  # 外层函数
    def inner():  # 内层函数
        print("我是one")
        f_ = f()  #
        print("添加功能1")
        return f_

    return inner  # 返回内层函数的地址


@out1
@out2
def show():
    print("hahaha")
    return 1


# 先从上到下，再从下到上
show()  # out1.inner(out2.inner(show)))
