from selenium import webdriver
from time import sleep
# 拿到浏览器驱动
brower_driver = webdriver.Firefox()
# 跳转网页
brower_driver.get("https://www.xdclass.net/")
# 验证title url
print(brower_driver.title)
print(brower_driver.current_url)
# 睡眠3秒
sleep(3)
brower_driver.find_element_by_xpath("/html/body/div/div/div[4]/div/div[2]/div[1]/a[4]/div/img").click()
