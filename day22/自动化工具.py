# -*- coding:utf-8 -*-
"""
使用selenium报错原因：
    1.浏览器加载失败，版本更新失败
    2.webdriver版本和要操作的浏览器版本相差过大
    3.代码有问题
1.导入模块 from selenium import webdriver
2.给加载程序添加无头浏览器
    webdriver.Chrome(executable_path="F:\pycharm\Python_qian\chromedriver.exe") #返回驱动器对象
3.所有的操作都建立在driver上

4.selenium的基本使用
    1.退出 close() quit()
    2.瞬间截图无头浏览器的加载界面
        save_screenshot()
    3.page_source查看网页源码
    4.get_cookies()获取cookies
5.selenium元素定位        //      数据仅限body中
    1.find_element_by_XXXX()返回第一个符合的元素
    2.find_elements_by_XXXX()返回列表
        *a.id
        *b.class_name
         c.link_text 通过文本内容获取数据
         d.tag_name 通过标签名字获取
        *e.xpath
6.使用自动化模拟人的行为
    向元素中输入数据：driver.find_element_by_id("kw").send_keys("马云")
    点击可以点的对象：driver.find_element_by_id("su").click()
7.页面等待技术
    使用time模块（内置模块）
    1.获取时间戳/时间节点
    2.让程序暂停
        time.sleep() 传入秒数
8.selenium执行js脚本
    通过驱动器的execute()执行js文件
9.切换窗口

"""
from selenium import webdriver
import time

w = webdriver.Chrome(executable_path="F:\pycharm\Python_qian\chromedriver.exe")  # 返回驱动器对象

# 使用get访问网站

w.get("http://www.1ppt.com/xiazai/jianli/ppt_jianli_1.html")
time.sleep(3)
print(w.find_element_by_class_name(""))
w.close()
