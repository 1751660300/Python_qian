# -*- coding:utf-8 -*-
import threading

# 创建一把互斥锁
lock = threading.Lock()


# 创建会死锁的任务
def show_num(index):  # 查看对应下标的元素
    g_list = [i for i in range(1, 5)]
    print(threading.current_thread().name)
    lock.acquire()
    if index >= len(g_list):
        print("下标越界")
        lock.release()  # 解决
        return
    print("该下标对应的值为：", g_list[index])
    lock.release()


if __name__ == '__main__':
    for i in range(10):
        th = threading.Thread(target=show_num, args=(i, ))
        th.start()
