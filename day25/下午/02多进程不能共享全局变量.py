# -*- coding:utf-8 -*-
import multiprocessing


g_list = []


def write():
    for i in range(10):
        g_list.append(i)
    print("append after is :", g_list)


def read():
    print("read data are :", g_list)


if __name__ == '__main__':
    w = multiprocessing.Process(target=write)
    r = multiprocessing.Process(target=read)
    w.start()
    r.start()