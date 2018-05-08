#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: add_new_ad_handler.py
Author: cwk
Date: 5/6/18
"""

import logging
import time
import json
import os

from src.biz.base_handler import BaseHandler
from src.biz import public_var
from src.biz import sql_pattern


class AddNewAdHandler(BaseHandler):

    def prepare(self):

        self.content_type = 'html'

    def get(self):

        self.render('new_ad.html')

    def post(self):
        """
        接收破碎通请求，在广告库中新建新的广告
        :return:
        """
        flag, param_dict = self.get_param_argument()
        if not flag:
            template_vars = {
                'code': public_var.WRONG_FORMAT,
                'msg': public_var.ERROR_MESSAGE[public_var.WRONG_FORMAT]
            }
            logging.debug("get param error: %s", str(template_vars))
            self.write(json.dumps(template_vars))
            return
        sql_handler = self.application.db_factory.get_instance(self.application.ad_biz_config,
                                                               'ad_mysql')
        flag, ad_id = self.update_db(sql_handler, param_dict)
        if flag:
            template_vars = {
                'code': public_var.RESULT_CODE_SUC,
                'msg': u'OK'
            }
            logging.info("add new ad success ad_id is %s", ad_id)
        else:
            template_vars = {
                'code': public_var.FAILED_MYSQL_INSERT,
                'msg': public_var.ERROR_MESSAGE[public_var.FAILED_MYSQL_INSERT]
            }
        self.write(json.dumps(template_vars))

    def get_param_argument(self):
        """
        获取请求参数
        :return:
        """
        base_url = 'localhost:9999/cpc_clk?positionId=%s'
        param_dict = dict()
        salary = self.get_body_argument('salary', None)
        salary_list = salary.split('-')
        if len(salary_list) != 2:
            return False, param_dict
        else:
            param_dict['salarymin'] = salary_list[0][0: 3]
            param_dict['salarymax'] = salary_list[1][0: 3]
        param_dict['companyName'] = self.get_body_argument('companyName', None)
        param_dict['positionfullName'] = self.get_body_argument('positionfullName', None)
        param_dict['positionName'] = self.get_body_argument('positionName', None)
        param_dict['city'] = self.get_body_argument('city', None)
        param_dict['positionAdvantage'] = self.get_body_argument('positionAdvantage', None)
        param_dict['workYear'] = self.get_body_argument('workYear', None)
        param_dict['request_url'] = self.get_body_argument('request_url', None)
        param_dict['priority'] = self.get_body_argument('priority', None)
        param_dict['clk_id'] = self.get_body_argument('clk_id', None)
        param_dict['stime'] = self.get_body_argument('stime', None)
        param_dict['etime'] = self.get_body_argument('etime', None)
        param_dict['stored'] = self.get_body_argument('stored', None)
        param_dict['cpc_spend'] = self.get_body_argument('cpc_spend', None)
        param_dict['record_url'] = base_url % param_dict['clk_id']
        logging.debug("param_dict is %s" % str(param_dict))
        return True, param_dict

    def update_db(self, sql_handler, param_dict):
        """
        更新数据库
        :param sql_handler:
        :param param_dict:参数
        :return:
        """
        db_name = self.application.ad_biz_config['ad_mysql']['db']
        tbl_name = 'ad_info'
        try:
            sql_handler.curs.execute(sql_pattern.get_next_primary_key, (tbl_name, db_name))
            ad_id = sql_handler.curs.fetchone()[0]
            query_args = (param_dict['companyName'], param_dict['positionfullName'],
                          param_dict['positionName'], param_dict['city'],
                          param_dict['positionAdvantage'], param_dict['salarymin'],
                          param_dict['salarymax'], param_dict['workYear'], param_dict['request_url'],
                          param_dict['record_url'], param_dict['priority'], param_dict['clk_id'],
                          param_dict['stime'], param_dict['etime'])
            sql_handler.curs.execute(sql_pattern.sql_insert_ad_data, query_args)
            sql_handler.curs.execute(sql_pattern.sql_insert_cpc_data, (ad_id, param_dict['stored'],
                                                                       param_dict['stored'],
                                                                       param_dict['cpc_spend']))
            sql_handler.conn.commit()
            return True, ad_id
        except Exception as e:
            sql_handler.conn.rollback()
            logging.error("insert data error", exc_info=True)
            return False, 0


if __name__ == '__main__':
    print "no process in __main__, %s" % os.path.realpath(__file__)
