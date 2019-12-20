import multiprocessing
import time
import os


def show_num():  # 20s
    for i in range(20):
        print("子进程：", i)
        print("子进程的PID:", os.getpid())
        print("子进程的PPID:", os.getppid())
        time.sleep(1)
        print("-" * 20)


if __name__ == '__main__':
    print("主进程开始")
    show_process = multiprocessing.Process(target=show_num)
    show_process.start()
    time.sleep(5)
    # 父进程死亡
    os.system('taskkill /F /PID {}'.format(os.getpid()))
    print("主进程结束")
    #  C:\Users\我是传奇\Desktop\武昌工学院\12月20日Python高级
    # cd 切换文件路径的
    # dir 查看当前路径下的所有问文件
