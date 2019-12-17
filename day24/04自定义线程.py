# -*- coding:utf-8 -*-
# 实现一个线程执行多个任务
import threading


class MyThread(threading.Thread):
    def __init__(self, count1, count2):
        self.count1 = count1
        self.count2 = count2
        super().__init__()

    def task(self):  # 任务1
        for i in range(self.count1):
            print("执行任务{}".format(i))

    def task2(self):  # 任务1
        for i in range(self.count2):
            print("执行任务{}".format(i))

    def run(self):
        self.task()
        self.task2()


if __name__ == '__main__':
    m = MyThread(5, 10)
    m.start()
    print(threading.current_thread())
