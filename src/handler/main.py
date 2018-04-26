#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: main.py
Author: cwk
Date: 4/13/18
"""

import logging
import json
import MySQLdb
from src.biz import sql_pattern
from src.biz.base_handler import BaseHandler
from src.biz import http_util


class MainHandler(BaseHandler):
    """主页"""

    def prepare(self):

        self.content_type = 'json'


    def get(self):

        sql_handler = self.application.db_factory.get_instance(self.application.ad_biz_config,
                                                               'ad_mysql')

        db_info = self.application.ad_biz_config['ad_mysql']
        db_info['charset'] = 'utf8'
        # self.db_info = db_info
        # logging.info('db_info is: %s' % db_info)
        # self.conn = MySQLdb.connect(host=self.db_info['host'], user=self.db_info['user'],
        #                             passwd=self.db_info['passwd'], db=self.db_info['db'],
        #                             charset=self.db_info['charset'])
        # curs = self.conn.cursor()
        try:
            logging.debug(sql_pattern.sql_select_test % ('Python', '西安'))
            # curs.execute(sql_pattern.sql_select_test, ('Python', '西安'))
            # rows = curs.fetchall()
            sql_handler.curs.execute(sql_pattern.sql_select_test, ('Python', '西安'))
            rows = sql_handler.curs.fetchall()
            logging.info("#################")
            self.write(json.dumps(rows, ensure_ascii=False, cls=http_util.CJsonEncoder))
        except Exception as e:
            logging.error("mysql error %s" % str(e), exc_info=True)


