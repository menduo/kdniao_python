#!/usr/bin/env python
# coding=utf-8
__doc__ = """
Example for using kdniao async clinet in tornado web app

run

$ python tornado_handler.py  --app_id={YourAppId} --app_key={YourAppKey}

then visit the links below:

http://127.0.0.1:19890/track?shipper_code=YTO&logistic_code=12345678

http://127.0.0.1:19890/recognise?shipper_code=YTO&logistic_code=12345678

http://127.0.0.1:19890/track_by_recognise?shipper_code=YTO&logistic_code=12345678
http://127.0.0.1:19890/track_by_recognise?shipper_code=YTO&logistic_code=A__12345678b__B
http://127.0.0.1:19890/track_by_recognise?shipper_code=YTO&logistic_code=a
"""

import sys

sys.path.insert(0, "..")

import os
import json
import tornado.web
import tornado.gen
import tornado.ioloop
from tornado.options import define, options, parse_command_line

define("app_id", type=int)
define("app_key", type=str)
define("port", type=int, default=19890)
define("debug", type=bool, default=True)
parse_command_line()

from kdniao import KdNiaoAsyncClient


class Env(object):
    API_ID = None
    API_KEY = None


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.async_client = KdNiaoAsyncClient(Env.API_ID, Env.API_KEY)

    def send_json(self, data):
        """
        send json data and set header
        """
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(data))
        self.finish()


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        res = __doc__
        res = res.replace("\n", "<br/>")
        return self.write(res)


class TrackHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        shipper_code = self.get_argument("shipper_code")
        logistic_code = self.get_argument("logistic_code")
        order_code = self.get_argument("order_code", "")
        resp = yield self.async_client.api_track.track(logistic_code, shipper_code, order_code)
        self.send_json(resp)


class TrackByRecogniseHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        logistic_code = self.get_argument("logistic_code")
        order_code = self.get_argument("order_code", "")

        res = yield self.async_client.api_recognise.recognise(logistic_code)
        shipper_list = res.get("data", {}).get("Shippers", [])

        shipper_code = None

        if shipper_list:
            shipper_code = shipper_list[0]["ShipperCode"]
        if not shipper_code:
            self.send_json({"data": {}})
            raise tornado.gen.Return()

        resp = yield self.async_client.api_track.track(logistic_code, shipper_code, order_code)
        self.send_json(resp)


class RecogniseHandler(BaseHandler):
    @tornado.gen.coroutine
    def get(self):
        logistic_code = self.get_argument("logistic_code")
        resp = yield self.async_client.api_recognise.recognise(logistic_code)
        self.send_json(resp)


app = tornado.web.Application(
    handlers=[
        ('/', IndexHandler),
        ('/track', TrackHandler),
        ('/track_by_recognise', TrackByRecogniseHandler),
        ('/recognise', RecogniseHandler),

    ],
    debug=options.debug,
)

if __name__ == '__main__':
    # Parse API id and key from the env and command line:
    _e = [app_id, app_key] = [
        os.environ.get("KDNIAO_APP_ID", ""),
        os.environ.get("KDNIAO_APP_KEY", "")
    ]

    if not all(_e):
        _e = [app_id, app_key] = [options.app_id, options.app_key]

    if not all(_e):
        raise ValueError("both app_id and app_key are required")

    Env.API_ID = app_id
    Env.API_KEY = app_key

    # Start our app:

    app.listen(options.port)
    print("\n\t Example for KdNiao Python SDK: please check http://127.0.0.1:%s\n" % options.port)
    tornado.ioloop.IOLoop.instance().start()
