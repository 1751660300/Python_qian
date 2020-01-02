# -*- coding:utf-8 -*-
from socket import *

so = socket(AF_INET, SOCK_STREAM)
so.bind(('', 8080))
so.listen()
client_so, port = so.accept()
data = client_so.recv(1024)
print(data.decode("gbk"))
reponse_line = "HTTP/1.1 200 ok\r\n"
reponse_header = "host:localhost\r\n"
with open("/root/PycharmProjects/Python_qian/day31/XiCi01.html", "r") as file:
    reponse_body = file.read()
client_so.send((reponse_line + reponse_header + "\r\n" + reponse_body).encode("utf-8"))
client_so.close()
so.close()
