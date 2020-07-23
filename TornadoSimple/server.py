import tornado.ioloop
import tornado.web
import tornado.options
import tornado.web

from tornado.options import define, options

define('port', default=8888, help="run on given port")

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        get_data = self.get_argument('data')
        self.set_cookie('bug-bounty', get_data)
        self.set_header('X-Requested-With', get_data)
        self.write("Hello Index: " + get_data)
    
    def head(self):
        get_data = self.get_argument('data')
        self.set_cookie('bug-bounty', get_data)
        self.set_header('X-Requested-With', get_data)
        self.write("Hello Index: " + get_data)



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")

tornado.options.parse_command_line()
app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(options.port)
tornado.ioloop.IOLoop.current().start()
