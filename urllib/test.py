from urllib.request import urlopen

if __name__ == '__main__':
    url = "http://www.baidu.com"
    resp = urlopen(url)

    with open("mybaidu.html", mode="w") as f:
        f.write(resp.read().decode("utf-8"))
    print("over!")
    resp.close()