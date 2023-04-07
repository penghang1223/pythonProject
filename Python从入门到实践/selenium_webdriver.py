from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element(By.ID, "kw").click()
driver.find_element(By.ID, "kw").send_keys("hello word")
driver.find_element(By.ID, "su").click()
# time.sleep(5)
# driver.back() #后退
# time.sleep(5)
# driver.forward() # 前进
# time.sleep(5)
# driver.refresh()# 刷新
# time.sleep(5)
# # driver.quit() # 退出
#
# driver.maximize_window() # 最大化窗口
# time.sleep(5)
# driver.minimize_window() # 最小化窗口


#
# Driver.set_window_position(坐标X, 坐标Y) #将浏览器窗口移动到指定位置
# Driver.set_window_size(宽度像素, 高度像素) #将浏览器窗口设置为指定大小
# Driver.set_window_rect(坐标X, 坐标Y, 宽度像素, 高度像素)#将浏览器窗口移动到指定位置，同时
# #设置窗口大小


driver.set_window_position(0, 0)
time.sleep(3)
driver.set_window_size(500, 300)
time.sleep(3)
driver.set_window_rect(100, 200, 600, 400)
print(driver.title)
print(driver.current_url)

# driver.title  #获取浏览器窗口当前的标题
# driver.current_url  #获取浏览器窗口当前的网址

# driver.get_window_position() #获取位置对象
# driver.get_window_size() #获取大小对象
# driver.get_window_rect() #获取位置及大小对象
