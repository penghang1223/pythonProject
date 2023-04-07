from selenium import webdriver

driver = webdriver.Chrome()

print("获取位置对象：", driver.get_window_position())
print("获取位置坐标x值：", driver.get_window_position()["x"])
print("获取位置坐标y值：", +driver.get_window_position()["y"])

print("获取大小对象：", driver.get_window_size())
print("获取宽度值", driver.get_window_size()["width"])
print("获取高度值", driver.get_window_size()["height"])

print("获取位置及大小对象：", driver.get_window_rect())
print("获取位置坐标x值：", driver.get_window_rect()["x"])
print("获取位置坐标y值：", driver.get_window_rect()["y"])
print("获取宽度值：", driver.get_window_rect()["width"])
print("获取高度值：", driver.get_window_rect()["height"])

#
# driver.get_window_position() #获取位置对象
# driver.get_window_size() #获取大小对象
# driver.get_window_rect() #获取位置及大小对象
