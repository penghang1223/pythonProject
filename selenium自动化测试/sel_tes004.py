from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


class MyCustomListener(AbstractEventListener):
    # driver.get("https://www.tao.com")
    def before_navigate_to(self, url, driver):
        print("页面在发生跳转前的URL为", driver.current_url)

    def after_navigate_to(self, url, driver):
        print("页面在发生跳转后的URL为", driver.current_url)

    def before_find(self, by, value, driver):
        print("查找元素时的条件为", by, value)

    def after_find(self, by, value, driver):
        print("找到元素，其条件为", by, value)

    def before_click(self, element, driver):
        print("要单击的页面元素为", element.get_attribute("value"))

    def before_click(self, element, driver):
        print("单击页面元素后的URL为", driver.current_url)

    def before_change_value_of(self, element, driver):
        print("更改前的值为", element.get_attribute("value"))

    def after_change_value_of(self, element, driver):
        print("更改后的值为", element.get_attribute("value"))

    def on_exception(self, exception, driver):
        driver.save_screenshot("D:\\error.png")
        print("发生异常", exception)
        print("截图已保存，地址为D:\\error.png")


driver = webdriver.Firefox()
eventDriver = EventFiringWebDriver(driver, MyCustomListener())

eventDriver.get("https://www.baidu.com/")

eventDriver.find_element(By.ID, "kw").send_keys("hello world")
eventDriver.find_element(By.ID, "su").click()
eventDriver.find_element(By.ID, "XXXXXX")  # 故意制造异常
