# -*- coding:utf-8 -*-
import time
import random
from multiprocessing import Process, Queue
import queue


def producer(queue):
    while True:
        queue.put(random.randint(1, 100))
        print("pro")


def consumer(queue):
    while True:
        if queue.empty():
            time.sleep(0.5)
        else:
            data = queue.get()
            print("con: ", data)


if __name__ == "__main__":
    # queue = queue.Queue()
    queue = Queue()
    queue.empty()
    my_producer = Process(target=producer, args=(queue,))
    my_consumer = Process(target=consumer, args=(queue,))
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()
