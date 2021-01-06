import tornado.web
import tornado.ioloop


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world this is python GET Request")


class carsRequestHander(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class queryRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if num.isdigit():
            r = "odd" if int(num) % 2 else "even"
            self.write(f"The integer {num} is {r}")

        else:
            self.write(f"{num} is not an integer")


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/cars", carsRequestHander),
        (r"/isEven", queryRequestHandler)
    ])

    port = 3000
    app.listen(port)
    print(f"Application running on {port}")
    tornado.ioloop.IOLoop.current().start()
