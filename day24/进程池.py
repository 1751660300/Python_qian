# -*- coding:utf-8 -*-
import multiprocessing
import time


def res1(queue):
    for i in range(10):
        queue.put(i)
        print("存入了数据")
        time.sleep(0.5)


def res2(queue):
    i = 0
    while True:
        while not queue.empty():
            print(queue.get())
            i += 1
        time.sleep(0.5)
        if i == 10:
            print(".........")
            break


if __name__ == '__main__':
    pool = multiprocessing.Pool(2)
    que = multiprocessing.Queue()
    pool.apply_async(res1, args=(que,))
    pool.apply_async(res2, args=(que,))
    pool.close()
    pool.join()
    print("完成")
