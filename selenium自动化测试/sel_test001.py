import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import ui

wait = ui.WebDriverWait(driver, 10)
driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

# move_to_element会将鼠标指针放置在"设置"链接上，实现悬停效果
ActionChains(driver).move_to_element(driver.find_element(By.XPATH, "//span[text()='设置']")).pause(3).perform()  #

ActionChains(driver).click(driver.find_element(By.LINK_TEXT, "搜索设置")).pause(3).perform()
# wait.until(lambda driver: driver.find_element(By.ID, "s1_2"))
ActionChains(driver).click(driver.find_element(By.ID, "s1_2")).click(driver.find_element(By.ID, "SL_2")).click(
    driver.find_element(By.ID, "sh_1")).click(driver.find_element(By.LINK_TEXT, "保存设置")).pause(3).perform()
