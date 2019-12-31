# -*- coding:utf-8 -*-
import socket

# 当前套接字使用ipv4通信，遵循tcp协议
so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

so.bind(('', 8090))
# so.connect(("127.0.0.1", 8080))
so.listen()
data = so.accept()
da = data[0].recv(1024)
data[0].send("GET / HTTP/1.1 200\r\n".encode("gbk"))
data[0].send("Host: 192.168.21.1:8090\r\n".encode("gbk"))
data[0].send("\r\n".encode("gbk"))
with open("XiCi01.html", "rb") as file:
    html = file.read()
    data[0].send(html)
print(data)
print(da)

