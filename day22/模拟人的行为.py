# -*- coding:utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="F:\pycharm\Python_qian\chromedriver.exe")

url = "https://accounts.douban.com/passport/login?source=movie"

try:
    driver.get(url)
    driver.find_element_by_id("username").send_keys("马云")
    time.sleep(3)
    driver.find_element_by_id("su").click()
    time.sleep(3)
    driver.execute()
# except Exception as e:
#     print(e)
finally:
    driver.quit()
