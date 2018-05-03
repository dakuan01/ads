#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: db_handler.py
Author: cwk
Date: 4/19/18
"""

import MySQLdb
import logging
import os


class MysqlDb(object):

    def __init__(self, db_info):
        db_info['charset'] = 'utf8'
        self.db_info = db_info
        self.conn = None
        self.curs = None
        self.init_db()

    def init_db(self):
        self.conn = MySQLdb.connect(host=self.db_info['host'], user=self.db_info['user'],
                                    passwd=self.db_info['passwd'], db=self.db_info['db'],
                                    charset=self.db_info['charset'])
        self.curs = self.conn.cursor()
        logging.info("init db %s" % str(self.db_info['db']))

    def destory(self):
        """destory db_conn"""
        self.conn.close()


if __name__ == '__main__':
    print "no process in __main__, %s" % os.path.realpath(__file__)
