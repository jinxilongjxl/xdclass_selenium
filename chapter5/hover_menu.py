# -*- coding:utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep
# 拿到driver
driver = webdriver.Firefox()
# 跳转网页
driver.get("https://www.xdclass.net/")
# 睡眠2秒等待网页加载
sleep(2)
# 定位鼠标移动到上面的元素
menu_ele = driver.find_element_by_css_selector(".list_item > li:nth-child(1)")
ActionChains(driver).move_to_element(menu_ele).perform()
# 选中子菜单
driver.find_element_by_css_selector(".base > div:nth-child(3) > a:nth-child(1)").click()


