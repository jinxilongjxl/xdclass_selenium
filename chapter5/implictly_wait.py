from selenium import webdriver
from time import sleep
# 获取驱动
driver = webdriver.Firefox()
# 登陆百度
driver.get("https://www.baidu.com/")
# 隐形等待最多5秒
driver.implicitly_wait(5)
# 打印title验证
print(driver.title)