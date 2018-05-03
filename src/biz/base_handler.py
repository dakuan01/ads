#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: base_handler.py
Author: cwk
Date: 4/12/18
"""

import logging
import os
import jieba
import time
from tornado.web import RequestHandler
import public_var
import sql_pattern


class BaseHandler(RequestHandler):

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def get_data_search(self, param):
        """
        根据搜索内容进行推荐
        :param param:
        :return: 查询状态和查询结果
        """
        seg_list = jieba.cut_for_search(param['info'])
        info_str = ','.join(seg_list)
        logging.debug(info_str)
        posNameList = list()
        cityList = list()
        for item in public_var.job_list:
            if item in info_str:
                posNameList.append(item)
        logging.debug('get posName is :%s' % str(posNameList))
        for item in public_var.city_list:
            if item in info_str:
                cityList.append(item)
        logging.debug('get city is :%s' % str(cityList))
        result = list()
        sql_handler = self.application.db_factory.get_instance(self.application.ad_biz_config,
                                                               'ad_mysql')
        date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        try:
            if len(cityList) == 0 and len(posNameList) > 0:
                for item in posNameList:
                    logging.debug(sql_pattern.sql_select_pos % (date, item, datetime, datetime))
                    sql_handler.curs.execute(sql_pattern.sql_select_pos, (date, item, datetime,
                                                                          datetime))
                    rows = sql_handler.curs.fetchall()
                    for row in rows:
                        result.append(row)
            elif len(cityList) > 0 and len(posNameList) == 0:
                for item in cityList:
                    logging.debug(sql_pattern.sql_select_city % (date, item, datetime, datetime))
                    sql_handler.curs.execute(sql_pattern.sql_select_city, (date, item, datetime,
                                                                           datetime))
                    rows = sql_handler.curs.fetchall()
                    for row in rows:
                        result.append(row)
            elif len(cityList) > 0 and len(posNameList) > 0:
                for city in cityList:
                    for posName in posNameList:
                        logging.debug(sql_pattern.sql_select_pos_city % (date, posName, city,
                                                                         datetime, datetime))
                        sql_handler.curs.execute(sql_pattern.sql_select_pos_city, (date, posName,
                                                                                   city, datetime,
                                                                                   datetime))
                        rows = sql_handler.curs.fetchall()
                        for row in rows:
                            result.append(row)
                result = sorted(result, key=lambda x: x[1])
            else:
                result = self.get_data_default()
        except Exception as e:
            logging.error('mysql error is :%s' % str(e), exc_info=True)
            return False, result
        result = self.conversion_type(result)
        return True, result

    def get_data_param(self, param):
        """
        根据职位或城市检索
        :param param:
        :return: 查询状态和查询结果
        """
        city = param['city']
        posName = param['posName']
        result = list()
        sql_handler = self.application.db_factory.get_instance(self.application.ad_biz_config,
                                                               'ad_mysql')
        date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        if city is not None:
            query_sql = sql_pattern.sql_select_city
            query_arg = (date, city, datetime, datetime)
        elif posName is not None:
            query_sql = sql_pattern.sql_select_pos
            query_arg = (date, posName, datetime, datetime)
        else:
            query_sql = sql_pattern.sql_select_pos_city
            query_arg = (date, posName, city, datetime, datetime)
        try:
            sql_handler.curs.execute(query_sql, query_arg)
            rows = sql_handler.curs.fetchall()
        except Exception as e:
            logging.error("mysql error:", exc_info=True)
            return False, result
        result = self.conversion_type(rows)
        return True, result

    def get_data_default(self):
        """
        在搜索时没有相关关键字时返回默认的广告
        :return:
        """
        result = list()
        return result

    def conversion_type(self, datas):
        """
        将list或tuple类型的数据修改为dict类型
        :param datas:
        :return:
        """
        result = list()
        for data in datas:
            item = dict()
            item['ad_id'] = data[0]
            item['companyName'] = data[1]
            item['positionfullName'] = data[2]
            item['positionName'] = data[3]
            item['city'] = data[4]
            item['positionAdvantage'] = data[5]
            item['salarymin'] = data[6]
            item['salarymax'] = data[7]
            item['workYear'] = data[8]
            item['request_url'] = data[9]
            item['record_url'] = data[10]
            item['priority'] = data[11]
            result.append(item)
        return result


if __name__ == '__main__':
    print "no process in __main__, %s" % os.path.realpath(__file__)
