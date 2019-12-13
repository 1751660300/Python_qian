# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup

file = open("F:\pycharm\Python_qian\myUtils\XiCi01.html", "r", encoding="utf-8")
data = file.read()
file.close()
b = BeautifulSoup(data, "lxml")
list = b.title
print(list)

# 1.使用.name直接获取对象 soup.title
soup = BeautifulSoup(' <b class="boldest">Extremely bold</b><b class = "boldest> Extremly bold bold</b>', 'lxml')
tag = soup.b
print(tag)
# 2.使用.name = new_name 会修改当前对象的name
tag.name = "blockquote"
print(soup)
# <blockquote class="boldest">Extremely bold</blockquote>
# <b class = "boldest> Extremly bold bold</b>

# 3使用attrs来赋值，和获取值，attrs获取所有的值，类似与字典，也可以使用get来或某个属性的值
print(list)
list["id"] = "as"
print(list.attrs["id"])
print(list.attrs)
print(list.get("id"))

# 4.每一个对象都包含name，就是标签的名字
print(list.name)

# 5.可以使用.string可以获取标签的内容,并且可以使用replace_with()替换内容
print(list.string, type(list.string))
list.string.replace_with("hahah")
list.string = "dedede"
print(list.string, type(list.string))

# 6.获取节点对象
# a.contents包含a标签节点下的节点
hd = b.head
print(hd.contents)

# b.strings获取所有的内容，stripped_strings不会输出多余的空白部分
for i in hd.stripped_strings:
    print(i)
print(hd.strings)

# c.使用find()和find_all()
# 参数:1.字符串
#      2.正则表达式
#      3.列表
#      4.方法，方法要有返回值
#      5.keyword



