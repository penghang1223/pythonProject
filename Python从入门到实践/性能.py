# from threading import Thread
# from selenium import webdriver
# import datetime
#
# import csv
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
#
# def baiduSearchHelloWorld(threadNumber):
#     driver = webdriver.Chrome()
#     # 记录页面加载的起始时间
#     page_load_start_time = datetime.datetime.now()
#     driver.get("https://www.baidu.com")
#     # 记录页面加载的结束时间
#     page_load_finish_time = datetime.datetime.now()
#     # 计算时间间隔，并添加到时间总计数中
#     load_time_span = page_load_finish_time - page_load_start_time
#     global total_load_time
#     total_load_time = total_load_time + load_time_span
#
#     # 记录搜索操作的起始时间
#     driver.find_element(By.ID, "kw").send_keys("hello world")
#     search_start_time = datetime.datetime.now()
#     driver.find_element(By.ID, "su").click()
#     # 等待含有hello world关键字的搜索结果出现
#     WebDriverWait(driver, 10, 0.1).until(EC.visibility_of_element_located((By.XPATH, "//a
#     [contains(text(), 'hello world')]")))"
#      # 记录搜索操作的结束时间
#     search_end_time = datetime.datetime.now()
#     # 计算时间间隔，并添加到时间总计数中
#     search_time_span = search_end_time - search_start_time
#     global total_search_time
#     total_search_time = total_search_time + search_time_span
#
#     driver.quit()
#     # 记录本次加载页面和搜索操作的执行时间
#     performance_data.append([threadNumber, load_time_span.total_seconds(), search_
#                              time_span.total_seconds()])
#
#     # 记录总时间的变量
#     total_load_time = datetime.timedelta()
#     total_search_time = datetime.timedelta()
#     # 记录各个线程的性能表现的数组
#     performance_data = []
#
#     # 并发数为20
#     tread_count = 20
#     threads = []
#
#     # 开启线程并执行
#     for threadNumber in range(tread_count):
#         t = Thread(target=baiduSearchHelloWorld, args=(threadNumber,))
#     threads.append(t)
#     t.start()
#
#     # 等待所有线程执行完毕
#     for t in threads:
#         t.join()
#
#     # 将收集到的性能数据输出到csv文件当中
#     csv_headers = ["线程号", "页面加载时间(秒)", "搜索执行时间(秒)"]
#     avg_performance_row = ["平均值", total_load_time.total_seconds() / tread_count, total_
#                            search_time.total_seconds() / tread_count]
#     with open("D:\\PerformanceTest.csv", "w", newline="", encoding="utf-8-sig") as f:
#         f_csv = csv.writer(f)
#     f_csv.writerow(csv_headers)
#     f_csv.writerows(performance_data)
#     f_csv.writerow(avg_performance_row)
