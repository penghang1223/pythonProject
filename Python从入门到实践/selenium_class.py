from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# searchTextBox = driver.find_element(By.CLASS_NAME,"s_ipt")
# link = driver.find_element(By.LINK_TEXT,"贴吧")   # 根据链接的文字进行匹配
link = driver.find_element(By.PARTIAL_LINK_TEXT, "贴")  # 相当于模糊匹配
# searchTextBox.send_keys("找到文本框")
link.click()
time.sleep(10)
