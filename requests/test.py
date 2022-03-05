import requests

if __name__ == '__main__':
    query = input("输入一个你选择的明星：")
    url = f'https://www.sogou.com/web?query={query}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
    }
    resp = requests.get(url, headers=headers)

    print(resp.text)
    resp.close()