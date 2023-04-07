import requests
from bs4 import BeautifulSoup
import os

# 创建目录以保存图像
if not os.path.exists('../images'):
    os.makedirs('../images')

# 获取网站页面内容
url = 'http://pic.netbian.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 获取图片标签
img_tags = soup.find_all('img')

# 遍历每个图片标签，并下载图片
for img in img_tags:
    # 获取图片链接
    img_url = url + img['src']
    # 下载图片
    response = requests.get(img_url)
    # 保存图片到本地
    with open('images/' + img['alt'] + '.jpg', 'wb') as f:
        f.write(response.content)
