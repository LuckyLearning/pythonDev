import requests

if __name__ == '__main__':
    url = "https://fanyi.baidu.com/sug"
    s = input("请输入要翻译的英文：")
    data = {
        "kw": s
    }
    resp = requests.post(url, data=data)
    print(resp.json())
    resp.close()