#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: cpc_clk_handler.py
Author: cwk
Date: 5/2/18
"""

import os
import logging

from src.biz.base_handler import BaseHandler


class CpcClkHandler(BaseHandler):

    def get(self):
        logging.debug("test")
        self.write('hello world')


if __name__ == '__main__':
    print "no process in __main__, %s" % os.path.realpath(__file__)
