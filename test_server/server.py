#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        page = open("site.html", "r")
        contents = page.read()
        page.close()
        self.write(contents)


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(80)
    tornado.ioloop.IOLoop.current().start()
