# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
# 拿到浏览器驱动
brower_driver = webdriver.Firefox()
# 跳转网页
brower_driver.get("https://www.xdclass.net/")
# 验证title url
print(brower_driver.title)
print(brower_driver.current_url)

sleep(3)
brower_driver.find_element_by_partial_link_text("学习").click()