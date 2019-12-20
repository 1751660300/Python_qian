# -*- coding:utf-8 -*-
import multiprocessing
import time


def puts(que):
    for i in range(10):
        queue.put(i)
        print("存取数据: ", i)
        time.sleep(1)


def gets(que):
    while True:
        time.sleep(1.5)
        if queue.empty():
            break
        print("读取数据:", queue.get())


if __name__ == '__main__':
    # 创建队列
    queue = multiprocessing.Queue(5)

    # 创建进程
    p1 = multiprocessing.Process(target=puts, args=(queue,))
    p2 = multiprocessing.Process(target=gets, args=(queue,))
    # 开始进程
    p1.start()
    p2.start()
    # p1.join()
    # p2.join()
