import requests
from lxml import etree

url = 'https://wuhan.zbj.com/search/f/?type=new&kw=SaaS'
if __name__ == '__main__':
    resp = requests.get(url)
    # print(resp.text)
    html = etree.HTML(resp.text)
    divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
    for div in divs:
        price = div.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")[0].strip('¥')
        title = 'SaaS'.join(div.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))
        com_name = div.xpath("./div/div/a[1]/div[1]/p/text()")[1].replace('\n\n', '')
        location = div.xpath("./div/div/a[1]/div[1]/div/span/text()")[0]
        print(location)
