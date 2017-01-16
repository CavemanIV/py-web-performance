import json, time
from tornado.httpserver import HTTPServer
from tornado.web import RequestHandler, Application
from tornado import ioloop

from burn import burn_cpu

# raw IOLoop version
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")

# def make_app():
#     return tornado.web.Application([
#         (r"/", MainHandler),
#     ])

# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)
#     import pdb; pdb.set_trace()  # FIXME: remove pdb point
#     i = tornado.ioloop.IOLoop.current()
#     i.start()


# TODO: change to @coroutine.gen
# HttpServer version
class TestHandler(RequestHandler):

    def get(self):
        rsp_time = burn_cpu()
        self.write(json.dumps({'elapse': rsp_time}))

application = Application([
    (r"/test", TestHandler),
])

if __name__ == '__main__':
    #application.listen(int(sys.argv[1]))
    #application.start(0)

    server = HTTPServer(application)
    server.bind(8080)
    server.start(None)
    ioloop.IOLoop.instance().start()
