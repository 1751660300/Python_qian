# -*- coding:utf-8 -*-
import time
import threading

g_list = []


def write():
    for i in range(5):
        g_list.append(i)
        print(i)
        time.sleep(1)
    print("写入数据：", g_list)


def read():
    print("读到的数据为：", g_list)


if __name__ == '__main__':
    w = threading.Thread(target=write)
    r = threading.Thread(target=read)
    w.start()
    w.join()
    r.start()
