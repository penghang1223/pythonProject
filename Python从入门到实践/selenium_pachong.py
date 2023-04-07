from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import csv

driver = webdriver.Chrome()
driver.implicitly_wait(5)

# 直接通过URL进入搜索结果页面
driver.get("https://www.epubit.com/search?txt=测试")
# 单击"图书"标签页
driver.find_element(By.XPATH, "//div[@class='tabs']/span[text()='图书']").click()

csvRows = []  # 用于存放各个图书信息的数组
number = 1  # 用于生成序号

# 收集所有搜索出来的图书
while True:
    # 等待Loading遮罩消失
    WebDriverWait(driver, 5).until_not(lambda d: driver.find_elements(By.ID, "el-loading-mask"))

# 获取页面上的每本图书的单元格
allSearchBooks = driver.find_elements(By.XPATH, "//div[@id='bookItem']/a")
# 收集每本图书的单元格上的书名与定价信息
for book in allSearchBooks:
    csvRows.append([number, book.find_element(By.CLASS_NAME, "list-title").text,
                    book.find_element(By.CLASS_NAME, "price").text])
    number = number + 1
    # 如果已翻到最后一页（即下一页按钮为禁用状态），则退出收集
    if len(driver.find_elements(By.XPATH, "//button[@class='btn-next disabled']")) > 0:
        break
# 单击"下一页"按钮
driver.find_element(By.XPATH, "//button[@class='btn-next']").click()

# 按照指定格式将收集到的数据输出到csv文件中
csvHeaders = ["序号", "名称", "价格"]
with open("C:\\TestBooks.csv", "w", newline="", encoding="utf-8-sig") as f:
    f_csv = csv.writer(f)
    f_csv.writerow(csvHeaders)
    f_csv.writerows(csvRows)
