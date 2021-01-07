import tornado.web
import tornado.ioloop
import json

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

class resourceRequestHandler(tornado.web.RequestHandler):
    def get(self, brandName, carId):
        self.write(f"Welcome, your car name is {brandName} and the number {carId}")


class carBrandsRequestHandler(tornado.web.RequestHandler):
    def get(self):
        fh = open("brands.txt", "r")
        brand = fh.read().splitlines()
        fh.close()
        self.write(json.dumps(brand))

    def post(self):
        brand = self.get_argument("brand")
        fh = open("brands.txt", "a")
        fh.write(f"{brand}\n")
        fh.close()
        self.write(json.dumps({"message": "Added successfuly!!"}))



if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/cars", carsRequestHander),
        (r"/isEven", queryRequestHandler),
        (r"/Brand/([a-z]+)/([0-9]+)", resourceRequestHandler),
        (r"/Brands", carBrandsRequestHandler)
    ])

    port = 3000
    app.listen(port)
    print(f"Application running on {port}")
    tornado.ioloop.IOLoop.current().start()
