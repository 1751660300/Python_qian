# -*- coding:utf-8 -*-
class ZongTong(object):
    def __init__(self):
        print("i am init")

    def __new__(cls, *args, **kwargs):
        print("i am new")
        # return object.__new__(cls)
        return object.__new__(cls)


if __name__ == '__main__':
    t = ZongTong()
