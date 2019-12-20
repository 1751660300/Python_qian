# -*- coding:utf-8 -*-
import multiprocessing
import time
import os


def dance(count):
    print(os.getppid())
    for i in range(count):
        print("123456", )
        time.sleep(1)


def sing(count):
    for i in range(count):
        print("唱歌")
        time.sleep(1)


if __name__ == '__main__':
    # 创建进程
    p1 = multiprocessing.Process(target=dance, args=(5, ))
    p2 = multiprocessing.Process(target=sing, args=(5, ))
    # 开始进程
    p1.start()
    p2.start()
    # 查看进程
    multiprocessing.current_process()
