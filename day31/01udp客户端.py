# -*- coding:utf-8 -*-
import socket
# 创建套接字
so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 确定客户端或服务端的ip地址和端口号，必须用元组进行封装

address = ('192.168.21.1', 8080)

# 发送数据

so.sendto("你好中国".encode("gbk"), address)

# 关闭套接字，是上下资源管理器，以免占用系统资源
so.close()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto("哈哈哈哈".encode("gbk"), ('192.168.1.100', 9090))
