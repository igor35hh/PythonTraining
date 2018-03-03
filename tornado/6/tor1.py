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
    def get(self):
        query = self.get_argument('q')
        client = tornado.httpclient.HTTPClient()
        
        #response  = client.fetch("https://api.twitter.com/1.1/search/tweets.json?"+urllib.urlencode({"q":query.encode('utf8'), 
                                #"result_type":"recent", "rpp":100}))
        #response  = client.fetch("http://www.faroo.com/api?q=iphone&start=1&length=10&l=en&src=web&f=json")
        response  = client.fetch("https://en.wikipedia.org/w/api.php?action=opensearch&search=pants&limit=3&format=json")
        body = json.loads(response.body)
        #result_count = len(body['results'])
        result_count = len(body)
        now = datetime.datetime.utcnow()
        #raw_oldest_tweet_at = body['results'][-1]['created_at']
        #oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at, "%a, %d %b %Y %H:%M:%S +0000")
        #seconds_diff = time.mktime(now.timetuple()) - time.mktime(oldest_tweet_at.timetuple())
        #tweets_per_second = float(result_count) / seconds_diff
        #tweets_per_second = 5
        
        self.write("""
            <div style="text-align: center">
                <div style="font-size: 72px">%s</div>
                <div style="font-size: 144px">%.02f</div>
                <div style="font-size: 24px">result count</div>
            </div>
        """ % (query, result_count))

    
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
                    
if __name__ == '__main__':
    main()
    