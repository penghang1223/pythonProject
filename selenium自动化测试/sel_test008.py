import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestEpubitCommon:
    def test_epubit_login(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)

        # 测试是否能够正确登录
        driver.get("https://www.epubit.com/")
        # 等待页面关键区域渲染完毕再操作
        WebDriverWait(driver, 5).until(lambda p: p.find_element(By.CLASS_NAME, "el-carousel__item"))
        driver.find_element(By.XPATH, "//i[text()='登录']").click()
        driver.find_element(By.ID, "username").send_keys("yibushequUser1")
        driver.find_element(By.ID, "password").send_keys("yibushequPwd1")
        driver.find_element(By.ID, "passwordLoginBtn").click()

        isJumpToHomePage = driver.current_url == "https://www.epubit.com/"
        isShowUserImg = len(driver.find_elements(By.CLASS_NAME, "userLogo")) > 0
        isShowLogout = len(
            driver.find_elements(By.XPATH, "//div[contains(@class,'logout')]/div[contains(text(),'退出')]")) > 0
        assert isJumpToHomePage and isShowUserImg and isShowLogout

        driver.quit()

    def test_book_search(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)

        driver.get("https://www.epubit.com/")
        driver.find_element(By.CLASS_NAME, "icon-sousuo").click()
        driver.find_element(By.XPATH, "//div[@class='searchBar']//input").send_keys("selenium")
        driver.find_element(By.XPATH, "//span[text()='搜索产品']/parent::button").click()
        allSearchBooks = driver.find_elements(By.XPATH, "//div[@id='bookItem']/a")
        hasResult = len(allSearchBooks) > 0
        allResultContainsKeyword = True
        for book in allSearchBooks:
            if "selenium" not in book.text.lower():
                allResultContainsKeyword = False
        assert hasResult and allResultContainsKeyword

        # 测试是否能够搜索关键字为python的图书
        driver.find_element(By.CLASS_NAME, "icon-sousuo").click()
        driver.find_element(By.XPATH, "//div[@class='searchBar']//input").send_keys("python")
        driver.find_element(By.XPATH, "//span[text()='搜索产品']/parent::button").click()
        allSearchBooks = driver.find_elements(By.XPATH, "//div[@id='bookItem']/a")
        hasResult = len(allSearchBooks) > 0
        allResultContainsKeyword = True
        for book in allSearchBooks:
            if "python" not in book.text.lower():
                allResultContainsKeyword = False
        assert hasResult and allResultContainsKeyword

        driver.quit()
