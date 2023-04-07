# driver.find_element_by_tag_name("input") #查找首个<input/>元素
# driver.find_element_by_tag_name("a")     #查找首个<a/>元素
# driver.find_element_by_tag_name("span")  #查找首个<span/>元素


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
# driver.find_element(By.TAG_NAME,"")   #  标签类型
# link = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/div/div[3]/ul/li[1]/a/span[2]")  # 觉得路径
link = driver.find_element(By.XPATH, '//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]')  # 双引号问题 改成单引号
link.click()
time.sleep(5)
