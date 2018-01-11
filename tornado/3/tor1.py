import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
import os.path
import random

define('port', default=8888, type=int, help='run on the given port')

class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r"/", IndexHandler),
            (r"/page", PostHadler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "web"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
        
class PostHadler(tornado.web.RequestHandler):
    def post(self):
        source_text = self.get_argument('source')
        text_to_change = self.get_argument('change')
        source_map = self.map_by_first_letter(source_text)
        change_lines = text_to_change.split('\r\n')
        self.render('page.html', source_map=source_map, change_lines=change_lines, choice=random.choice)
        
    def map_by_first_letter(self, text):
        mapped = dict()
        for line in text.split('\r\n'):
            for word in [x for x in line.split(' ') if len(x)>0]:
                if word[0] not in mapped:
                    mapped[word[0]] = []
                mapped[word[0]].append(word)
        return mapped
    
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
                    
if __name__ == '__main__':
    main()
    