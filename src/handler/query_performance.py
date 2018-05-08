#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: query_performance.py
Author: cwk
Date: 5/7/18
"""

import os
import logging

from src.biz.base_handler import BaseHandler
from src.biz import sql_pattern
from src.biz import public_var

class Query_Performance(BaseHandler):

    def prepare(self):

        self.content_type = 'html'

    def get(self):

        self.render('query_performance.html')

    def post(self):

        ad_id = self.get_body_argument('ad_id', None)
        types_of = self.get_body_argument('type', None)
        logging.debug('ad_id is %s, type is %s' % (ad_id, types_of))
        sql_handler = self.application.db_factory.get_instance(self.application.ad_biz_config,
                                                               'ad_mysql')
        result = list()
        if types_of == 'num':
            sql_handler.curs.execute(sql_pattern.sql_select_cpc, [ad_id])
            rows = sql_handler.curs.fetchall()
            for row in rows:
                item = {
                    'num': row[0],
                    'date': row[1]
                }
                result.append()
            template_vars = {
                'title': u'点击数据',
                'data': result
            }
            self.make_return(public_var.RESULT_CODE_SUC, template_vars, 'OK', 'result_cpc.html')
        elif types_of == 'ban':
            sql_handler.curs.execute(sql_pattern.sql_select_ban, [ad_id])
            row = sql_handler.curs.fetchone()
            template_vars = {
                'title': u'余额',
                'ban': row[0]
            }
            self.make_return(public_var.RESULT_CODE_SUC, template_vars, 'OK', 'result_ban.html')


if __name__ == '__main__':
    print "no process in __main__, %s" % os.path.realpath(__file__)
