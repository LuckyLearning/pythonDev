import requests
import re
import csv

url = "https://movie.douban.com/chart"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
}
if __name__ == '__main__':
    resp = requests.get(url, headers=headers)
    content = resp.text
    # print(content)

    obj = re.compile(r'<table.*?<a class="nbg".*?title="(?P<name>.*?)">.*?<p class="pl">'
                     r'(?P<date>.*?)/.*?<span class="rating_nums">'
                     r'(?P<score>.*?)</span>.*?'
                     r'<span class="pl">\((?P<num>.*?)\)', re.S)
    res = obj.finditer(content)
    f = open("data.csv", mode="w")
    csvWriter = csv.writer(f)
    for i in res:
        # print(i.group("name"))
        # print(i.group("date").strip())
        # print(i.group("score"))
        # print(i.group("num"))
        dic = i.groupdict()
        dic['date'] = i.group("date").strip()
        csvWriter.writerow(dic.values())
    f.close()
    print("over!")