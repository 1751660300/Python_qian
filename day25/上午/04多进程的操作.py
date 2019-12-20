import multiprocessing  # 进程模块
import time
import os


def sing():  # 耗时5秒
    # 子进程的
    # print("sing进程", multiprocessing.current_process().pid)
    print("当前sing进程的PID：", os.getpid())
    print("当前sing进程的PPID：", os.getppid())
    for i in range(5):
        print("唱歌{}".format(i))
        time.sleep(1)


def dance():  # 耗时5秒
    # print("dance进程", multiprocessing.current_process().pid)
    print("当前dance进程的PID：", os.getpid())
    print("当前dance进程的PPID：", os.getppid())
    for i in range(5):
        print("跳舞{}".format(i))
        time.sleep(1)


if __name__ == '__main__':
    # 测试入口开始的地方----主进程的开始
    # print(multiprocessing.current_process().pid)
    print("当前主进程的PID：", os.getpid())
    print("当前主进程的PPID：", os.getppid())
    # 使用多进程实现多任务
    # 1.先创建子进程
    sing_process = multiprocessing.Process(target=sing)
    dance_process = multiprocessing.Process(target=dance)
    # 2.启动子进程
    sing_process.start()
    dance_process.start()

# 对于02.py程序来说
# 有几个线程几个进程  3   3

