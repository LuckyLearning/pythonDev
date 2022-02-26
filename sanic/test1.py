'''
Author: lifan
Date: 2022-02-26 06:52:55
Description: sanic测试文件
'''

from sanic import Sanic, json, text


app = Sanic('test1')


@app.route('/')
async def main_page(request):
    # return text('hello')
    print('----------:' + request.ip)
    return json({'id': '001', 'name': [[1, 2],
                                       3, 4]})

app.run(host='127.0.0.1', port='8000', debug=True)
