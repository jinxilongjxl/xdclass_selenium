from selenium import webdriver
# 拿到浏览器驱动
brower_driver = webdriver.Firefox()
# 跳转网页
brower_driver.get("https://www.baidu.com/")
# 验证title url
print(brower_driver.title)
print(brower_driver.current_url)
# 选中输入框，输入小D课堂
brower_driver.find_element_by_id('kw').send_keys("小D课堂")
# 选中按钮，触发点击事件
brower_driver.find_element_by_id("su").click()

eles = brower_driver.find_element_by_tag_name("input")
print(eles)
