import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
import os.path
import random
import time

from pymongo import MongoClient

define('port', default=8888, type=int, help='run on the given port')

class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r"/", IndexHandler),
            (r"/recommended/", RecommendedHandler),
            (r"/book/([0-9Xx\-]+)", BookHandler),
            (r"/edit/([0-9Xx\-]+)", AddEditHandler),
            (r"/delete/([0-9Xx\-]+)", DeleteHandler),
            (r"/add/", AddEditHandler),
            (r"/discussion/", DiscussionHandler),
            (r'/login', LoginHandler),
            (r'/logout', LogoutHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "web"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            ui_modules={"Book": BookModule},
            cookie_secret = "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
            login_url='/login',
            debug=True,
        )
        
        conn = MongoClient("mongodb://localhost:27017")
        self.db = conn["bookstore"]
        tornado.web.Application.__init__(self, handlers, **settings)
        
class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie('username')
        
class LogoutHandler(BaseHandler):
    
    @tornado.web.authenticated
    def get(self):
        if (self.get_argument('logout', None)):
            self.clear_cookie('username')
            self.redirect('/')
        
class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')
    
    def post(self):
        username = self.get_argument("username", "")
        password = self.get_argument("password", "")
        
        print(username, password)
        
        if username and password:
            coll = self.application.db.users
            user = dict()
            user = coll.find_one({"user": username})
            if user:
                if password == user["password"]:
                    self.set_secure_cookie('username', self.get_argument('username'))
                else:
                    self.clear_cookie('username')
            else:
                coll.insert({"user": username, "password":password}) 
                self.set_secure_cookie('username', self.get_argument('username'))
               
        self.redirect('/')
        
        
class DeleteHandler(BaseHandler):
    
    @tornado.web.authenticated
    def post(self, isbn=None):
        coll = self.application.db.books
        if isbn:
            coll = self.application.db.books
            book = coll.find_one_and_delete({"isbn":isbn})
            self.redirect("/recommended/")
            return
        self.set_header(404)
        return
        
class BookHandler(BaseHandler):
    
    @tornado.web.authenticated
    def get(self, isbn=None):
        if isbn:
            coll = self.application.db.books
            book = coll.find_one({"isbn":isbn})
            if 'comments' in book:
                comments = book['comments']
            else:
                comments = {}
            if book:
                self.render(
                    'one_book.html',
                    page_title = "Burt's Books | " + book['title'],
                    header_text = book['title'],
                    book=book,
                    comments=comments,
                    user=self.current_user,
                )
                return
        self.set_header(404)
        return
    
    @tornado.web.authenticated
    def post(self, isbn=None):
        coll = self.application.db.books
        book = dict()
        
        if isbn:
            book = coll.find_one({"isbn": isbn})
            
            book['isbn'] = self.get_argument('isbn', None)
            
            if 'comments' in book:
                data_book = book['comments']
            else:
                data_book = {}
            dict_data = {
                str(random.randint(1000,9999)):{'author':self.get_argument('author', None), 'comment':self.get_argument('comment', None)}
            }
            data_book.update(dict_data)
            
            book['comments'] = data_book
            
            coll.save(book)
            
            self.redirect("/book/%s" % isbn)
            
        else:
            self.set_header(404)
            return 
        
class AddEditHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, isbn=None):
        book = dict()
        if isbn:
            coll = self.application.db.books
            book = coll.find_one({"isbn":isbn})
        self.render(
            'book_edit.html',
            page_title = "Burt's Books | Home",
            header_text = "Edit book",
            book=book,
            user=self.current_user,
        )
    
    @tornado.web.authenticated
    def post(self, isbn=None):
        book_fields = ['isbn', 'title', 'subtitle', 'image', 'author', 'date_released', 'description']
        coll = self.application.db.books
        book = dict()
        
        if isbn:
            book = coll.find_one({"isbn": isbn})
            
        for key in book_fields:
            book[key] = self.get_argument(key, None)
            
        if isbn:
            coll.save(book)
        else:
            book['date_added'] = int(time.time())
            coll.insert(book)
        
        self.redirect("/recommended/")
        

class IndexHandler(BaseHandler):
    
    def get(self):
        self.render(
            'index.html',
            page_title = "Burt's Books | Home",
            header_text = "Welcome to Burt's Books!",
            user=self.current_user,
        )
        
class BookModule(tornado.web.UIModule):
    def render(self, book):
        return self.render_string("modules/book.html", book=book)
    
    def css_files(self):
        return "css/recommended.css"
    
    def javascript_files(self):
        return "js/recommended.js"
        
class RecommendedHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        coll = self.application.db.books
        books = coll.find()
        self.render('recommended.html', 
                    page_title = "Burt's Books | Recommended Reading",
                    header_text = "Recommended Reading", 
                    books=books,
                    user=self.current_user,
        )
        
class DiscussionHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        coll = self.application.db.books
        books = coll.find()
        comments={}
        for book in books:
            if 'comments' in book:
                comments.update(book['comments'])
                
        self.render(
            "discussion.html",
            page_title = "Burt's Books | Discussion",
            header_text = "Talkin' About Books With Burt",
            comments=comments,
            user=self.current_user,
        )
    
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
                    
if __name__ == '__main__':
    main()
    