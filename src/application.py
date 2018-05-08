#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: application.py
Author: cwk
Date: 4/12/18
"""


import logging
import os
import signal
import socket
import time
import traceback

import jinja2
import tornado.gen
import tornado.httpclient
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.web import Application

from src.handler.main import MainHandler
from src.handler.ad_recommend_handler import AdRecommendHandler
from src.handler.cpc_clk_handler import CpcClkHandler
from src.handler.add_new_ad_handler import AddNewAdHandler
from src.handler.query_performance import Query_Performance

io_loop = None
http_server = None


def debug(signal, frame):
    """
        brief info for: debug
            debug handler，将当前栈信息写入profile.pid文件
            有需要的话，可以通过开启InteractiveConsole，进入Python Console调试
        Args:
            signal: signal.signal传入的识别信号
            frame: signal.signal传入的stack frame
        Return: None
        Raise: None
    """

    d = {'_frame': frame}  # Allow access to frame object.
    d.update(frame.f_globals)  # Unless shadowed by global
    d.update(frame.f_locals)

    ts = time.strftime('%H:%M:%S', time.localtime(time.time()))

    message = "=== " + str(os.getpid()) + " " + ts + " ===\n"
    message += ''.join(traceback.format_stack(frame))
    message += "===\n"
    with open("profile." + str(os.getpid()), 'a+') as f:
        f.write(message)


def stop_http(signum, frame):
    """ stop_http """
    global http_server
    global io_loop

    # 不接收新的 HTTP 请求
    logging.info("run stop HTTPServer")
    http_server.stop()

    # 处理完现有的 callback 和 timeout 后，可以跳出 io_loop.start() 里的循环
    logging.info("run stop IOLoop")
    io_loop.stop()


def listen_signal():
    """
        brief info for: listen_signal
            给SIGUSR1信号加上一个debug handler
            给SIGUSR2信号加上一个stop handler
    """
    signal.signal(signal.SIGUSR1, debug)
    signal.signal(signal.SIGUSR2, stop_http)


def start_http(service_name, hostid, http_config, ad_biz_config, db_factory):
    """start http"""

    listen_signal()

    global io_loop
    global http_server
    global application

    # generate application
    global HANDLERS

    handlers = HANDLERS
    application = App(service_name, hostid, http_config['port'],
                      handlers,
                      http_config,
                      ad_biz_config,
                      db_factory,
                      http_config['template'])
    application.req_id = 0
    if 'timeout' in http_config:
        application.timeout = http_config['timeout']
    else:
        # default
        application.timeout = 5000
    io_loop = tornado.ioloop.IOLoop.instance()
    http_server = tornado.httpserver.HTTPServer(application, io_loop=io_loop, xheaders=True)
    http_server.bind(http_config['start_hostids'][hostid], backlog=1023)
    http_server.start(1)

    logging.info("Tornado Application[Service: %s] Started, Address: %s:%s" % (service_name,
                                                                               socket.gethostbyname(socket.gethostname()),
                                                                               http_config['start_hostids'][hostid]))
    # start io_loop
    io_loop.start()


class App(Application):
    """ App """

    def __init__(self, service_name, hostid, out_port,
                 handlers,
                 http_config,
                 ad_biz_config,
                 db_factory,
                 template_path=None):
        """ init sth"""
        self._hostid = hostid
        self.http_config = http_config
        self.ad_biz_config = ad_biz_config
        self.db_factory = db_factory

        settings = {
            'out_port': out_port,
            'service_id': service_name,
            'host_id': str(self._hostid),
            'compress_response': True,
            "login_url": "/",
            "template_path": template_path
        }
        logging.debug(str(settings))
        Application.__init__(self, handlers, **settings)

        self.region = self.http_config.get('region', "china")
        self.jinja_env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True,
                                            loader=jinja2.FileSystemLoader(
                                                settings['template_path']))


HANDLERS = [
    (r'/', MainHandler),
    (r'/ad_re', AdRecommendHandler),
    (r'/cpc_clk', CpcClkHandler),
    (r'/add_new_ad', AddNewAdHandler),
    (r'/query', Query_Performance)
]

if __name__ == "__main__":
    print "no process in __name__ of %s" % os.path.realpath(__file__)
    pass
