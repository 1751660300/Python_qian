# -*- coding:utf-8 -*-
import threading
import time


def sing():
    for i in range(3):
        print("唱歌{}".format(i))
        time.sleep(1)


if __name__ == '__main__':
    sing_thread = threading.Thread(target=sing, daemon=True)
    sing_thread1 = threading.Thread(target=sing)  # 设置守护
    sing_thread1.setDaemon(True)
    sing_thread.start()  # 开始线程
    sing_thread1.start()
    sing_thread.join()  # 阻塞主线程，当前线程执行完成后释放主线程
