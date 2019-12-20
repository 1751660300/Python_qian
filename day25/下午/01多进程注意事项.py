# -*- coding:utf-8 -*-
"""
1.多进程注意事项
    a.主进程等待子进程
    让进程设置守护 multiprocessing.Process(target=dance, daemon=True)
    进程对象p2.daemon = True
"""
import multiprocessing
import time


def dance():
    for i in range(5):
        print("123456", )
        time.sleep(1)


def sing():
    for i in range(5):
        print("唱歌")
        time.sleep(1)


if __name__ == '__main__':
    # 创建进程
    p1 = multiprocessing.Process(target=dance, daemon=True)
    p2 = multiprocessing.Process(target=sing)
    p2.daemon = True
    # 开始进程
    p1.start()
    p2.start()
    p1.terminate()  # 销毁子进程
    p1.join()
    p2.join()
    print("理想状态下退出")
