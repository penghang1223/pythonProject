from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

baiduSearchInput = driver.find_element(By.ID, "kw")
baiduSearchInput.send_keys("hello world")
time.sleep(3)  # 等待3s，以便容易看到界面的变化
baiduSearchInput.send_keys(Keys.CONTROL, "a")  # 全选
time.sleep(3)
baiduSearchInput.send_keys(Keys.CONTROL, "x")  # 剪切
time.sleep(3)
baiduSearchInput.send_keys(Keys.CONTROL, "v")  # 粘贴
time.sleep(3)
baiduSearchInput.send_keys(Keys.BACKSPACE)  # 删除
time.sleep(3)
baiduSearchInput.send_keys(Keys.ENTER)
