# -*- coding:utf-8 -*-
import socket
# 当前套接字使用ipv4通信，遵循tcp协议
so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

so.bind(('', 8010))
# so.connect(("127.0.0.1", 8080))
so.connect(("10.50.7.23", 8080))
while True:
    # so.send("给阿姨倒一杯卡布奇洛，开始你的炸弹秀！！！！".encode("gbk"))
    i = input()
    so.send(i.encode("gbk"))
    print("发送成功！")








