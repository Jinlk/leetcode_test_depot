# 该脚本目的是为了爬取资源，代码中的网址皆为示例
import os

import requests
from bs4 import BeautifulSoup

destination_folder = 'C:\Desktop'  # 爬取资源存放的位置
# 基础 URL
base_url = "https://www.abc.com/book/123456/"  # 你要访问的网址
headers = {
    # 请求头
    'User-Agent': 'Movvlla/5.0 (Winnbs NT 10.0; Win84; x84) AppleWebKit/537.36 (KHTML, like Gecko) Chroyou/133.0.1.0 Sawbri/568.49',
    'Referer': 'https://www.abc.com/bule/123456/'
}

# 检查目录是否存在，不存在则创建
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 发送请求获取章节列表页面
response = requests.get(base_url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# 找到所有章节链接
chapter_links = [a['href'] for a in soup.find_all('a', href=True)]

# 该对象是为了防止chapter_link是别的而导致程序错误，得自己观察网页的url拼接
target_start = '/blue/123456/'

# 遍历章节链接并下载内容
for chapter_link in chapter_links:
    if chapter_link.startswith(target_start):
        chapter_url = "https://www.abc.com" + chapter_link
        chapter_response = requests.get(chapter_url)
        while chapter_response.status_code != 200:
            if chapter_response.status_code == 502:
                print(f"章节 {chapter_url} 访问状态码为 502，重试中...")
                chapter_response = requests.get(chapter_url)
            else:
                print(f"章节 {chapter_url} 访问状态码为 {chapter_response.status_code}，异常情况，跳过。")
                break
        if chapter_response.status_code == 200:
            chapter_soup = BeautifulSoup(chapter_response.content, 'html.parser')
            content = chapter_soup.find('div', class_='content').text
            chapter_title = chapter_soup.find('h1').text
            chapter_file_path = os.path.join(destination_folder, f"{chapter_title}.txt")
            if os.path.exists(chapter_file_path):
                print(f"章节 {chapter_title} 已存在，跳过下载。")
            else:
                print(f"正在下载章节: {chapter_title}")
                with open(chapter_file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
