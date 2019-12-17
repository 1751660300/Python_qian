# -*- coding:utf-8 -*-
import time
import threading

g_list = 0
lock = threading.Lock()  # 创建锁


def write1():
    global g_list
    lock.acquire()  # 上锁
    for i in range(10):
        g_list += i
        time.sleep(0.5)
    print("写入数据：", g_list)
    lock.release()  # 释放锁


def write2():
    global g_list
    lock.acquire()
    for i in range(10):
        g_list += i
        time.sleep(0.5)
    print("写入数据：", g_list)
    lock.release()


if __name__ == '__main__':
    w1 = threading.Thread(target=write1)
    w2 = threading.Thread(target=write2)
    w1.start()
    # w1.join()  # 使用join解决
    w2.start()
    print(g_list)
