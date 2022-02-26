import re

if __name__ == '__main__':
    # 匹配字符串中所以的符合项
    # list = re.findall(r"\d+", "tom的电话10086，jay的电话10010")
    # print(list)

    # finditer 迭代器
    # it = re.finditer(r"\d+", "tom的电话10086，jay的电话10010")
    # for i in it:
    #     print(i)
    #     print(i.group())

    # search 找到一个结果就返回，返回的是match对象，需要group拿数据
    # s = re.search(r"\d+", "tom的电话10086，jay的电话10010")
    # print(s.group())

    # match是从头开始匹配
    # s = re.match(r"\d+", "10086，jay的电话10010")
    # print(s.group())

    # 预加载正则表达式
    # obj = re.compile(r"\d+")
    #
    # ret = obj.finditer("tom的电话10086，jay的电话10010")
    # for i in ret:
    #     print(i.group())

    s = """
    <div class='class1'><span id='1'>张三</span></div>
    <div class='class1'><span id='2'>李四</span></div>
    <div class='class1'><span id='3'>王五</span></div>
    """
    # (?P<分组名字>正则)
    # re.S: .能匹配换行
    obj = re.compile(r"<div class='(?P<class>.*?)'><span id='(?P<id>.*?)'>(?P<group1>.*?)</span></div>", re.S)
    res = obj.finditer(s)
    for i in res:
        print(i.group("class"))
        print(i.group("id"))
        print(i.group("group1"))