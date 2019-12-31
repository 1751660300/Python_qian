# -*- coding:utf-8 -*-
import pymysql


con = pymysql.connect(host='localhost', port=3306, database='mysql', user='root', password='123456', charset='utf8')
cur = con.cursor()
data = cur.execute("select * from user;")
print(cur.connection)
print(cur.fetchall())
cur.close()
con.close()