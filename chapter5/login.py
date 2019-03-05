# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver = webdriver.Firefox()
driver.get("https://www.xdclass.net/")
# 查找登陆元素
login_ele = driver.find_element_by_css_selector(".login > span:nth-child(1)")
# 点击登陆元素
ActionChains(driver).click(login_ele).perform()
# 弹出登录框后
# 查找输入手机号元素
phone_num_ele = driver.find_element_by_css_selector(".mobienum > input:nth-child(1)")
phone_num_ele.clear()
phone_num_ele.send_keys("15201866828")
# 查找输入密码元素
phone_pwd_ele = driver.find_element_by_css_selector(".psw > input:nth-child(1)")
phone_pwd_ele.clear()
phone_pwd_ele.send_keys("1qazxsw2")
# 查找登陆按钮元素，并点击
sub_login_ele = driver.find_element_by_css_selector(".btn")
sub_login_ele.click()
# 判断登陆是否成功
# 查找登陆成功后的头像元素
user_ele = driver.find_element_by_css_selector(".avatar_img")
# 出发hover事件
ActionChains(driver).move_to_element(user_ele).perform()
# 获取用户名称元素
user_name_ele = driver.find_element_by_css_selector(".username")
print("===============测试结果=============")
if u"TenSleep" == user_name_ele.text: # 如果比较的字符串带中文，前面要加u
    print("登陆成功！！")