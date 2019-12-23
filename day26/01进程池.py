# -*- coding:utf-8 -*-
import multiprocessing
import time
import os


# 创建一个函数打印工作两个字
def task(i):
    print(os.getpid(), ":工作中{}.....".format(i))
    time.sleep(1)
    print("使用cpu时间", time.process_time())


if __name__ == '__main__':
    # 创建10个task进程
    pool = multiprocessing.Pool(6)  # 使用当前电脑的两个cpu
    tm = time.struct_time(time.gmtime())
    print(tm.tm_sec)
    for i in range(10):
        pool.apply(task, args=(i, ))
    print(tm.tm_sec)
    print(os.cpu_count())