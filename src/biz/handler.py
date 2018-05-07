#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: handler.py
Author: cwk
Date: 5/3/18
"""

import os
import logging
import time
import json

from tornado.web import RequestHandler

import public_var


class Handler(RequestHandler):

    def __init__(self, application, request, **kwargs):
        super(Handler, self).__init__(application, request, **kwargs)

        self.content_type = 'json'

    def make_return(self, result_code, result, err_msg, template_name=None,
                    http_status=public_var.HTTP_OK):
        """  make_return """
        ret = dict()
        ret['req_id'] = self.application.req_id
        ret['result_code'] = result_code
        ret['timestamp'] = str(long(time.time()))
        ret['err_msg'] = err_msg
        for key in result.keys():
            ret[key] = result[key]
        logging.debug("ret is %s" % json.dumps(ret))
        # logging.debug("content_type is " % self.content_type)
        if self.content_type == 'json' or template_name is None:
            self.set_status(public_var.HTTP_OK)
            self.set_header('Content-Type', 'application/json')
            self.write(ret)
        else:
            self.render2(template_name, **ret)


if __name__ == '__main__':
    print "no process in __main__, %s" % os.path.realpath(__file__)
