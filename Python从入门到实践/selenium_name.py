import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
# searchTextBox = driver.find_element(By.ID, "wd")
time.sleep(10)
# searchTextBox.send_keys("找到文本框")
driver.find_element(By.CLASS_NAME, "title-content-title").click()
# driver.close()
