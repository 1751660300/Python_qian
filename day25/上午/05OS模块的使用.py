import os

# 创建一个文件夹  mkdir(即使用于Linux又适用于windows)
# os.mkdir("./haha")
# print(os.cpu_count())

# 获取pid  os.getpid()
# 获取当前进程的编号
print(os.getpid())
# 获取父进程的编号 PPID
# os.getppid()
# Pychame的进程号8912
# print(os.getppid())  # 操作系统的进程编号
print(os.system("dir"))
# https://www.cnblogs.com/apollo1616/p/9510322.html
