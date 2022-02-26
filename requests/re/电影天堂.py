import requests

domain = "https://m.dytt8.net/index2.htm"

if __name__ == '__main__':
    resp = requests.get(domain, verify=False) #verify=False 去掉安全验证
    resp.encoding = "gb2312"
    print(resp.text)