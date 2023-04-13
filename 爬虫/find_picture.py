# 第二版
# -*-coding:utf-8-*-
import os
import re
import time
import requests
import bs4
from bs4 import BeautifulSoup

# 手动写入目标套图的首页地址
download_url = "www.mmzztt.com"

# 这里不需要手动输入页面数量了，可以通过解析首页地址得到总页面数
# page_num = 25

# 文件保存的绝对路径(D:\imgae\test_file)，注：这个路径上面的文件夹一定是要已经创建好了的，不然运行会报错
file_path = "C:\\picture"

# 文件名通过网页得到，注：以网页上套图的名字命名
file_name = " "

# 目标图片下载地址的前半部分，注：固定不变那部分，后半段是变化的，需要解析网页得到
imgae_down_url_1 = "https://s.iimzt.com/thumb"
# data-src="https://s.iimzt.com/thumb/85681/480.jpg"
# 修改请求headers以伪装成浏览器访问，从而绕开网站的反爬机制获取正确的页面，注：这个需要根据自己浏览器的实际的信息改
headers = {
    "User-Agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}


# 访问网页并返回HTML相关的信息
def getHTMLText(url, headers):
    # 向目标服务器发起请求并返回响应
    try:
        r = requests.get(url=url, headers=headers, timeout=20)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, "html.parser")
        return soup
    except:
        return ""


# 获取该套图的名称和总页面数
def getFileName(url, headers):
    # 从目标地址上面获取套图的名称
    soup = getHTMLText(url, headers)
    head1 = soup.find_all("header")
    h1 = head1[1].find_all("h1")
    name = h1[0].text
    pagination = soup.find_all("div", "pagination")
    a = pagination[0].find_all("a")
    page = int(a[len(a) - 2].text)
    return name, page


# 创建文件夹
def CreateFolder(file_name):
    flag = True
    num = 0
    while flag == 1:
        if num <= 0:
            file = file_path + '\\' + file_name  # 如果文件夹不存在，则创建文件夹
        else:
            file = file_path + '\\' + str(num) + '_' + file_name  # 如果文件夹已存在，则在文件夹前面加上数字，防止覆盖掉以前保存过的文件
        if not os.path.exists(file):
            os.mkdir(file)
            flag = False
        else:
            print('该文件名已存在，已重新命名')
            flag = True
            num += 1
            # time.sleep(1)
    # 返回文件存放的路径
    path = os.path.abspath(file) + '\\'
    return path


# 下载图片
def DownloadPicture(url, img_num, path):
    # 访问目标网址
    soup = getHTMLText(url, headers)

    # 解析网址，提取目标图片相关信息，注：这里的解析方法是不固定的，可以根据实际的情况灵活使用
    p = soup.find_all("p")
    tag = p[0].find_all("img")  # 得到该页面目标图片的信息

    # 下载图片
    for i in range(0, len(tag)):
        if (tag[i].attrs['src'] != None):
            # 解析网址，得到目标图片的下载地址
            imgae_down_url_2 = tag[i].attrs['src']  # 获取目标图片下载地址的后半部分
            imgae_url = imgae_down_url_1 + imgae_down_url_2  # 把目标图片地址的前后两部分拼接起来，得到完整的下载地址
            print("imgae_url: ", imgae_url)
            # 给图片命名
            img_num += 1
            name = tag[i].attrs['alt'] + '_' + str(img_num)  # 获取img标签的alt属性，用来给保存的图片命名，图片格式为jpg
            img_name = name + ".jpg"
            # 下载图片
            timeout = 5  # 超时重连次数
            while timeout > 0:
                try:
                    img_data = requests.get(url=imgae_url, headers=headers, timeout=30)
                    # 保存图片
                    img_path = path + img_name
                    with open(img_path, 'wb') as fp:
                        fp.write(img_data.content)
                    print(img_name, "******下载完成！")
                    timeout = 0
                except:
                    print(img_name, "******等待超时，下载失败！")
                    time.sleep(1)
                    timeout -= 1
    return img_num


# 主函数
if __name__ == "__main__":
    # 记录下载时间
    start = time.time()

    # 检查网址，如果输入的网址不是首页，则改成首页地址
    result = download_url.find('_')
    if (result != -1):
        new_str = ''
        check_flag = 1
        for i in range(0, len(download_url)):
            if (download_url[i] != '_' and check_flag):
                new_str = new_str + download_url[i]
            else:
                if (download_url[i] == '_'):
                    check_flag = 0
                if (download_url[i] == '.'):
                    new_str = new_str + download_url[i]
                    check_flag = 1
        download_url = new_str
        print("new download_url: ", download_url)

    # 创建保存数据的文件夹
    file_name, page_num = getFileName(download_url, headers)  # 获取套图名称
    print("page_num: ", page_num)
    path = CreateFolder(file_name)
    print("创建文件夹成功: ", path)

    # 按页下载图片
    image_num = 0  # 当前累计下载图片总数
    for i in range(0, int(page_num)):
        if i == 0:
            page_url = download_url  # 首页网址，注：因为这个网站首页和后面那些页面网址的规则不一样，所以这里要区分开来
        else:
            page_url = download_url[:-5] + "_" + str(i) + ".html"  # 第2页往后的网址，都是用数字来排布页面
        # 下载图片
        print("page_url: ", page_url)
        image_num = DownloadPicture(page_url, image_num, path)
        # image_num = num  # 每下载完一页图片就累计当前下载图片总数

    print("全部下载完成！", "共" + str(len(os.listdir(path))) + "张图片")

    # 打印下载总耗时
    end = time.time()
    print("共耗时" + str(end - start) + "秒")
