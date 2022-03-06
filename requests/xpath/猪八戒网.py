
import requests
from lxml import etree

url = 'https://wuhan.zbj.com/search/f/?type=new&kw=SaaS'
resp = requests.get(url)
# print(resp.text)
html = etree.HTML(resp.text)
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]")
for div in divs: 
    price = div.xpath("./div/div/div/a[2]/div[2]/div[1]/span[1]/text()")[0].strip('￥')
    title = div.xpath("./div/div/div/a[2]/div[2]/div[2]/p/text()")
    com_name = div.xpath("./div/div/div/a[1]/div[1]/p/text()")
    location = div.xpath("./div/div/div/a[1]/div[1]/div/span/text()")
    print(price)