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
brower_driver.find_element_by_css_selector(".hotcourse > div:nth-child(2) > a:nth-child(1) > div:nth-child(1) > img:nth-child(2)").click()
