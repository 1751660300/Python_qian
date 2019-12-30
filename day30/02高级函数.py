# -*- coding:utf-8 -*-
list1 = [1, 2, 3, 4]


# map函数
# 1.给函数一个参数
# 2.要返回计算后的结果
def com(i):
    return i ** 2


for i in map(com, list1):
    print(i)


# filter函数
def filt(i):
    return i % 2 == 0


for i in filter(filt, list1):
    print(i)

# reduce
from functools import reduce


def add(a, b):
    return a + b


print(reduce(add, list1))
