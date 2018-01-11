import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
import os.path

define('port', default=8888, type=int, help='run on the given port')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
        
class PostHadler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('page.html', roads=noun1, wood=noun2, made=verb, difference=noun3)
        
                    
if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/", IndexHandler),
        (r"/page", PostHadler),
    ],
        template_path=os.path.join(os.path.dirname(__file__), "web")
    )
    
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()