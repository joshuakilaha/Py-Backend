import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world this is python GET Request")


class carsRequestHander(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/cars",carsRequestHander)
    ])

    port = 3000
    app.listen(port)
    print(f"Application running on {port}")
    tornado.ioloop.IOLoop.current().start()
