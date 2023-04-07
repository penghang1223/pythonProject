from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
searchTextBox = driver.find_element(By.ID, "wd")
searchTextBox.send_keys("找到文本框")
