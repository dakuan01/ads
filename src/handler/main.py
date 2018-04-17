#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: main.py
Author: cwk
Date: 4/13/18
"""

import logging
from src.biz.base_handler import BaseHandler


class MainHandler(BaseHandler):
    """主页"""

    def get(self):

        self.write("hello world")
