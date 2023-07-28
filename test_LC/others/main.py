from flask import Response
from werkzeug import run_simple


class Flask(object):
    def __call__(self, environ, start_responses):
        print("请求来了")

    # self()调用 Flask __call__ 方法
    def run(self):
        run_simple(hostname='localhost', port=9999, application=self)


def func(environ, start_response):
    print("一个请求")
    return Response("A")


if __name__ == '__main__':
    # app = Flask()
    # app.run()
    #app()

    # func()
    run_simple(hostname='localhost', port=9999, application=func)
