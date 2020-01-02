# -*- coding:utf-8 -*-
import pymysql


class MySql(object):
    __instance = None
    __cursor = None
    __flag = 0

    def __init__(self):
        if self.__flag == 0:
            self.host = "localhost"
            self.port = 3306
            self.database = "san_guo"
            self.user = "root"
            self.password = "mysql"
            self.charset = "utf8"
            self.__flag = 1

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def get_cursor(self):
        if self.__cursor is None:
            self.con = pymysql.connect(host="localhost", port=3306, database="mysql", user="root", password="mysql",
                                       charset="utf8")
            self.__cursor = self.con.cursor()  # 创建游标
        return self.__cursor

    def close(self):
        self.__cursor.close()
        self.con.close()
