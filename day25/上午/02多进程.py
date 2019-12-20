# -*- coding:utf-8 -*-
import multiprocessing
import time


def dance():
    print("123456", )
    time.sleep(1)


def sing():
    print("唱歌")
    time.sleep(1)


if __name__ == '__main__':
    # 创建进程
    p1 = multiprocessing.Process(target=dance)
    p2 = multiprocessing.Process(target=sing)
    # 开始进程
    p1.start()
    p2.start()
    p1.join()
    p2.join()


    # update mysql.user set password=PASSWORD("123456") where User="root"