# -*- coding:utf-8 -*-
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="F:\pycharm\Python_qian\chromedriver.exe")

url = "https://www.baidu.com/"

try:
    driver.get(url)
    driver.find_element_by_id("kw").send_keys("马云")
    time.sleep(3)
    driver.find_element_by_id("su").click()
    time.sleep(3)
    driver.execute_script("alert('小青蛙')")
    time.sleep(3)
    win_list = driver.window_handles
    print(win_list)
    driver.switch_to.window(win_list[0])
    time.sleep(3)
    driver.switch_to.frame()
# except Exception as e:
#     print(e)
finally:
    driver.quit()
