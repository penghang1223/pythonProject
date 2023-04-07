from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
searchTextBox = driver.find_element(By.ID, "kw")
searchTextBox.send_keys("找到文本框")
