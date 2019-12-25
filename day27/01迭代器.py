# -*- coding:utf-8 -*-
# 创建一个可迭代对象
# python3.6导入模块方式  from collections import Iterable
from collections.abc import Iterable


class MyList(object):
    def __init__(self, _list):
        self._list = _list

    def __iter__(self):
        return MyListIterator(self._list)  # 传输数据


class MyListIterator(object):  # 标准的迭代器类
    def __init__(self, _list):
        self._list = _list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.index += 1
            if self.index > len(self._list):
                raise StopIteration
            else:
                return self._list[self.index-1]


if __name__ == '__main__':
    my_list = MyList([1, 2, 3])
    print("my_list是否为迭代对象", isinstance(my_list, Iterable))  # 验证是否为迭代对象 方法一 isinstance(my_list, Iterable)

    for i in my_list:  # 验证是否为迭代对象 方法二 是否可以写for循环
        print(i)