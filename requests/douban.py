
import requests

url = "https://movie.douban.com/j/chart/top_list?"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
}

if __name__ == '__main__':
    param = {
        "type": 24,
        "interval_id": "100:90",
        "action": "",
        "start": 0,
        "limit": 20
    }
    resp = requests.get(url, params=param, headers=headers)
    data = resp.json()
    print(data)
    print(len(data))
    resp.close()

