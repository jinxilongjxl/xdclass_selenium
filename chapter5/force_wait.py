from selenium import webdriver
from time import sleep
# 获取驱动
driver = webdriver.Firefox()
# 登陆百度
driver.get("https://www.baidu.com/")
# 强制等待
sleep(5)
# 打印title验证
print(driver.title)