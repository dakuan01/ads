#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: cpc_clk_handler.py
Author: cwk
Date: 5/2/18
"""

import os
import time
import logging

from src.biz.base_handler import BaseHandler
from src.biz import sql_pattern


result = """
<html>
<head>
<script>
window.back()
</script>
</head>
</html>
"""



class CpcClkHandler(BaseHandler):

    def prepare(self):

        self.content_type = 'html'

    def get(self):

        positionId = self.get_argument('positionId', None)
        ad_id = self.get_argument('ad_id', None)
        logging.debug('position id is %s, ad_id is %s' % (positionId, ad_id))
        sql_handler = self.application.db_factory.get_instance(self.application.ad_biz_config,
                                                               'ad_mysql')
        date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        try:
            logging.debug(sql_pattern.sql_update_cpc_num % (positionId, date, ad_id))
            logging.debug(sql_pattern.sq_update_cpc_balance % ad_id)
            sql_handler.curs.execute(sql_pattern.sql_update_cpc_num, (positionId, date, ad_id))
            sql_handler.curs.execute(sql_pattern.sq_update_cpc_balance, [ad_id])
            sql_handler.conn.commit()
        except Exception as e:
            logging.error("update db error", exc_info=True)
        self.write(result)


if __name__ == '__main__':
    print "no process in __main__, %s" % os.path.realpath(__file__)
