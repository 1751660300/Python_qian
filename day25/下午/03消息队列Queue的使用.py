# -*- coding:utf-8 -*-
import multiprocessing
from multiprocessing import JoinableQueue

queue = multiprocessing.Queue(3)  # 最大容量为3
# 存放数据
queue.put(1)
queue.put("123")
queue.put((1, ))  # 已经满了
print(queue.full())
print(queue.qsize())
print(queue.get())
print(queue.qsize())
print(queue.get())
print(queue.qsize())
print(queue.get())
print(queue.qsize())
print(queue.empty())
print(queue.get_nowait())
