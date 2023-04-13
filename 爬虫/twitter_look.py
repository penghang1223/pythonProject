import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://twitter.com/home"
driver.get(url)
# 隐式等待，等页面元素稳定后就定位
driver.implicitly_wait(30)
# 找到用户名输入框并输入用户名
driver.find_element(By.XPATH,
                    '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(
    "tianyouyao")
# 隐式等待，等页面元素稳定后就定位
driver.implicitly_wait(10)
# 点击下一步
driver.find_element(By.CSS_SELECTOR, ".css-18t94o4:nth-child(6) > .css-901oao > .css-901oao > .css-901oao").click()
# 输入密码
driver.find_element(By.NAME, "password").send_keys("ihyin20200726")
# 登录
driver.find_element(By.CSS_SELECTOR, ".r-1inkyih > .css-901oao").click()

driver.find_element(By.CSS_SELECTOR, ".r-30o5oe").click()
driver.find_element(By.CSS_SELECTOR, ".r-majxgm > .css-901oao").click()
# 模拟鼠标滚轮，滑动页面至底
js = "window.scrollTo(0, document.body.scrollHeight)"
driver.execute_script(js)
# 不关闭浏览器
ActionChains(driver).key_down(Keys.CONTROL).send_keys("t").key_up(Keys.CONTROL).perform()
# i = 0
# while i < 1000:
# speed = 3  # speed控制下滑幅度
# js = "window.scrollTo(" + str(i) + ',' + str(i + speed) + ");"  # 模拟鼠标下滑的js语句
# i += speed
# driver.execute_script(js)  # 执行js语句
# time.sleep(random.randint(0, 1))  # 控制下滑频率
