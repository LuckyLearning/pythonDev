import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
}
url = "https://image.baidu.com/search/index?ct=&tn=baiduimage&word=性感"
resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"
print(resp.text)
main_page = BeautifulSoup(resp.text, "html.parser")
liList = main_page.find("ul", class_="imglist clearfix pageNum0").find("li")
print(liList)