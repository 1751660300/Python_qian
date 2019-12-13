# -*- coding:utf-8 -*-
from myUtils import ProxiesUtils
import time
from multiprocessing import *


def st(queue, Flag):
    d_list = []
    print("主线程方法：", queue)
    while Flag:
        while True:
            if queue.empty():
                break
            dic = queue.get()
            d_list.append(dic)
        if len(d_list) > 5:
            Flag = False
            print("开始工作了")
            print(Flag)
        else:
            print("等待。。。。")
            print("d_list的长度为",len(d_list))
            time.sleep(0.5)


if __name__ == '__main__':
    data_list = list()
    queue = Queue()
    print("主进程：", queue)
    flag = True
    url = "https://www.baidu.com/"
    ps1 = Process(target=st, args=(queue, flag))
    ps2 = Process(target=ProxiesUtils.getProxies, args=(queue, url))
    ps2.start()
    ps1.start()
    ps1.join()
    ps2.join()
