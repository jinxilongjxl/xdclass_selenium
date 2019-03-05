from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 获取驱动
driver = webdriver.Firefox()
# 登陆百度
driver.get("https://www.baidu.com/")
# 显性等待最大5s，每隔0.5s看看有没有找到id为kw的元素，
# 如果有则向下执行，否则继续等待，超时的话报异常
input_ele = WebDriverWait(driver,5,0.5).until(EC.presence_of_all_elements_located((By.ID,"kw")))
# 打印title验证
print(driver.title)