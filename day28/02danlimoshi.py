# -*- coding:utf-8 -*-
class w(object):
    __instance = None
    __flag = 0

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__flag == 0:
            self.__flag = 1
            print("i am init")


if __name__ == '__main__':
    p1 = w()
    p2 = w()
    print(id(p1))
    print(id(p2))
