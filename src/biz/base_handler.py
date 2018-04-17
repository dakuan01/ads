#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: base_handler.py
Author: cwk
Date: 4/12/18
"""

import logging
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)


if __name__ == '__main__':
    pass
