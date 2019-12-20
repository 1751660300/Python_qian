# -*- coding:utf-8 -*-
"""
1.线程的注意点
    a.线程调用是随机的
    b.
2.阻塞线程
    卡时间点
    子线程.join()
3.自定义线程
import threading


class MyThread(threading.Thread):
    def __init__(self, count):
        self.count = count
        super().__init__()

    def task1(self):
        pass

    def task2(self):
        pass

    def run(self):
        self.task1()
        self.task2()
自定义线程开启使用start
4.多线程共享变量
    存在问题：资源竞争
    解决：使用join，让一部分线程先跑完
        使用互斥锁
5.互斥锁
    lock = threading.Lock,返回一个对象
    lock.acquire()  # 上锁
    lock.release()  # 释放锁
"""
import threading


class MyThread(threading.Thread):
    def __init__(self, count):
        self.count = count
        super().__init__()

    def task1(self):
        pass

    def task2(self):
        pass

    def run(self):
        self.task1()
        self.task2()
