# -*- coding:utf-8 -*-
import time
import threading


def song(s):
    for i in range(3):
        time.sleep(1)
        print("{}:唱歌ing {}".format(s, i))


if __name__ == '__main__':
    # 创建线程：threading.Thread(target=song, args=("cxk",)) 返回一个线程对象
    # 状态：已经执行，只是在休眠中
    print(threading.enumerate())
    t1 = threading.Thread(target=song, args=("cxk",), name="cxk")
    t2 = threading.Thread(target=song, kwargs={"s": "wkq"}, name="wkq")

    # 启动线程
    t1.start()
    t2.start()
    # 获取线程列表
    print(threading.enumerate())  # 当前正在执行的线程列表
    print(threading.current_thread())  # 主线程开始的列表
    for i in range(10):
        print(i)
