from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestEpubitCommon:
    def test_epubit_login_success(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get("https://www.epubit.com/")
        # 等待页面关键区域渲染完毕再操作
        WebDriverWait(driver, 5).until(lambda p: p.find_element(By.CLASS_NAME,
                                                                "el-carousel_item"))
        driver.find_element(By.XPATH, "//i[text()='登录']").click()
        driver.find_element(By.ID, "username").send_keys("yibushequUser1")
        driver.find_element(By.ID, "password").send_keys("yibushequPwd1")
        driver.find_element(By.ID, "passwordLoginBtn").click()

        # 比较预期结果与实际结果
        is_jump_to_home_page = driver.current_url == "https://www.epubit.com/"
        is_show_user_img = len(driver.find_elements(By.CLASS_NAME, "userLogo")) > 0
        is_show_logout = len(
            driver.find_elements(By.XPATH, "//div[contains(@class,'logout')]/div[contains(text(),'退出')]")) > 0
        assert is_jump_to_home_page and is_show_user_img and is_show_logout

        driver.quit()
