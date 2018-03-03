import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

import urllib, json, datetime, time

from tornado.options import define, options

define('port', default=8000, type=int, help='run on the given port')

class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r"/", IndexHandler),
        ]
        settings = dict(
            #template_path=os.path.join(os.path.dirname(__file__), "web"),
            #static_path=os.path.join(os.path.dirname(__file__), "static"),
            #ui_modules={"Book": BookModule},
            debug=True,
        )
        
        tornado.web.Application.__init__(self, handlers, **settings)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        query = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()
        response  = yield tornado.gen.Task(
            client.fetch, 
            "https://en.wikipedia.org/w/api.php?action=opensearch&search=pants&limit=3&format=json")
        
        body = json.loads(response.body)
        result_count = len(body)
        now = datetime.datetime.utcnow()
        self.write("""
            <div style="text-align: center">
                <h4>Async gen engine</h4>
                <div style="font-size: 72px">%s</div>
                <div style="font-size: 144px">%.02f</div>
                <div style="font-size: 24px">result count</div>
            </div>
        """ % (query, result_count))
        self.finish()

    
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
                    
if __name__ == '__main__':
    main()
    