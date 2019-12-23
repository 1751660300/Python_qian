# -*- coding:utf-8 -*-
import multiprocessing
# from multiprocessing import shared_memory
import time
import os


# 创建一个函数打印工作两个字
def task(i):
    print(os.getpid(), ":工作中{}.....".format(i))
    print("开始使用cpu时间{}:".format(i), time.process_time())
    time.sleep(1)
    print("结束使用cpu时间{}:".format(i), time.process_time())


if __name__ == '__main__':
    # 创建10个task进程
    pool = multiprocessing.Pool(2)  # 使用当前电脑的两个cpu
    tm = time.struct_time(time.gmtime())
    print(tm.tm_sec)
    for i in range(10):
        pool.apply_async(task, args=(i,))
    pool.close()
    pool.join()  # 阻塞主进程
    print("主进程使用的时间:", time.process_time())


