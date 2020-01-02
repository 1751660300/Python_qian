# -*- coding:utf-8 -*-
import pymysql


with pymysql.connect(host="localhost", port=3306, database="mysql", user="root", password="mysql",
                                       charset="utf8") as con:
    print(con)

