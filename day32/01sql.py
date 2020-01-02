# -*- coding:utf-8 -*-
from day32 import cur


mysql = cur.MySql()
curs = mysql.get_cursor()
sql = 'insert into hero(name, guo_ji) values (\'司马老贼\', \'魏国\');'
shan = 'delete from hero where id = 2;'
update = 'update hero set id=2 where name="貂蝉"'
se = 'select * from user'
curs.execute(se)
mysql.con.commit()
data = curs.fetchall()
for i in data:
    print(i)
mysql.close()


