import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
import textwrap

define('port', default=8888, type=int, help='run on the given port')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'hello')
        self.write(greeting + ', dear user')
        
class ReverseHandler(tornado.web.RedirectHandler):
    def get(self, input):
        self.write(input[::-1])
        
class WrapHadler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))
        
class ErrorHandler(tornado.web.RequestHandler):
    def write_error(self, status_code, **kwargs):
        self.write("You caused a %d error" % status_code)
        
                                
if __name__ == '__main__':
    tornado.options.parse_command_line()
    #{"url": "/{1}/{0}/{2}"}
    app = tornado.web.Application(handlers=[
        (r"/index", IndexHandler),
        (r"/error", ErrorHandler),
        (r"/reverse/(\w+)", ReverseHandler, {"url": "/{0}/{1}"}),
        (r"/wrap", WrapHadler)
    ])
    
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    
    
    
    