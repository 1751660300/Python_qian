# -*- coding:utf-8 -*-
import socket
so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定客户端的ip地址和端口
so.bind(('', 8080))
data = so.recvfrom(1024)
# 发送数据确认用户






