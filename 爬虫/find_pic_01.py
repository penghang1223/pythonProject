import re
import requests
import os
import time

''' 爬取的彼岸桌面的壁纸'''
# 总页模板
urls = 'http://www.netbian.com/meishi/index_{}.htm'

# 找出user-agent代理 模拟登入
headers = {
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

# 创建保存图片的文件夹
if not os.path.exists("C:\picture"):
    os.mkdir("C:\picture")

# 爬取前5页
for i in range(1, 6):
    # 加入time.sleep 推迟线程 防止爬取频率过快 ，后台异常
    time.sleep(1)
    # 第一页的特殊，单独标记起来
    if i == 1:
        main_url = 'http://www.netbian.com/meishi/index.htm'
    # 除第一页的
    else:
        main_url = urls.format(i)
    print('--------------------------')
    # get请求，获取每一页面的url
    response = requests.get(main_url, headers=headers)
    # 获取每一页网页代码文本信息
    html = response.text
    # 正则匹配 ，(.*?) 用于分组只显示src，不显示alt，防止乱码， .*? 全匹配  ，都是非贪婪匹配
    img_urls = re.findall(r'<img src="(.*?)" alt=".*?">', html)
    for url in img_urls:
        # 图片名字，对url进行截取，负索引；
        img_name = url.split('/')[-1]
        # get请求，获取页面中图片的url
        response = requests.get(url, headers=headers)
        with open("C:\meishi\Images\{}".format(img_name), "wb") as file:
            # 保存图片
            file.write(response.content)
