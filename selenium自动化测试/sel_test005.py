from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.implicitly_wait(5)
driver.get("https://www.epubit.com/")

# 等待页面关键区域渲染完毕再操作
WebDriverWait(driver, 5).until(lambda p: p.find_element(By.CLASS_NAME, "el-carousel__item"))
driver.find_element(By.XPATH, "//i[text()='登录']").click()
driver.find_element(By.ID, "username").send_keys("yibushequUser1")
driver.find_element(By.ID, "password").send_keys("yibushequPwd1")
driver.find_element(By.ID, "passwordLoginBtn").click()
# 比较预期结果与实际结果
isJumpToHomePage = driver.current_url == "https://www.epubit.com/"  # 当前网页地址等于这个则为true
isShowUserImg = len(driver.find_elements(By.CLASS_NAME, "userLogo")) > 0  # 有userlogo则为true
isShowLogout = len(
    driver.find_elements(By.XPATH, "//div[contains(@class,'logout')]div[contains(text(),'退出')]")) > 0  # 有推出按钮则true
if not isJumpToHomePage or not isShowUserImg or not isShowLogout:  # 三个有一个为false  则输出异常
    raise Exception("Login failed!")

driver.quit()
