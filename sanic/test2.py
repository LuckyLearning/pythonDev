'''
Author: lifan
Date: 2022-02-26 09:26:56
Description: Class Based View
'''
from sanic import response, text
from sanic.response import redirect
from sanic import Sanic
from sanic.views import HTTPMethodView

app = Sanic('test2')

class SimpleView(HTTPMethodView):

  def get(self, request):
      return text("I am get method")

  # You can also use async syntax
  async def post(self, request):
      return text("I am post method")

  def put(self, request):
      return text("I am put method")

  def patch(self, request):
      return text("I am patch method")

  def delete(self, request):
      return text("I am delete method")

app.add_route(SimpleView.as_view(), "/")

class NameView(HTTPMethodView):

  def get(self, request, name):
    return text("Hello {}".format(name))

app.add_route(NameView.as_view(), "/<name>")

@app.route("/redirect")
def index(request):
    print('------redirect')
    url = app.url_for("SpecialClassView")
    return redirect(url)

class SpecialClassView(HTTPMethodView):
    def get(self, request):
        print('------spe')
        return text("Hello from the Special Class View!")

app.add_route(SpecialClassView.as_view(), "/special_class_view")


app.run(host='0.0.0.0', debug=True)
