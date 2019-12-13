# -*- coding:utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome(executable_path="F:\pycharm\Python_qian\chromedriver.exe")

url = "https://baidu.com/"

try:
    driver.get(url)
    title_name = driver.find_element_by_link_text("新闻")
    print(title_name.get_attribute("href"))
    driver.get(title_name.get_attribute("href"))

# except Exception as e:
#     print(e)
finally:
    driver.quit()
