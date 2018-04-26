#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: db_util.py
Author: cwk
Date: 4/19/18
"""

import os

from db_handler import MysqlDb


class DbHandlerFactory(object):
    """ DbHandlerFactory """

    def __init__(self):
        self.handler_dict = dict()

    def get_instance(self, conf_dict, handler_name):
        """ get_instance """
        self.handler_dict[handler_name] = MysqlDb(conf_dict[handler_name])
        return self.handler_dict[handler_name]


if __name__ == "__main__":
    print "no process in __main__, %s" % os.path.realpath(__file__)
