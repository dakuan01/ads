#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: base_handler.py
Author: cwk
Date: 4/12/18
"""

import logging
import jieba
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
        try:
            if len(cityList) == 0 and len(posNameList) > 0:
                for item in posNameList:
                    sql_handler.curs.execute(sql_pattern.sql_select_pos, [item])
                    result.append(sql_handler.curs.fetchall())
            elif len(cityList) > 0 and len(posNameList) == 0:
                for item in cityList:
                    sql_handler.curs.execute(sql_pattern.sql_select_city, [item])
                    result.append(sql_handler.curs.fetchall())
            elif len(cityList) > 0 and len(posNameList) > 0:
                for city in cityList:
                    for posName in posNameList:
                        sql_handler.curs.execute(sql_pattern.sql_select_pos_city, (posName, city))
                        result.append(sql_handler.curs.fetchall())
            else:
                pass
        except Exception as e:
            logging.error('mysql error is :%s' % str(e), exc_info=True)
            return False, result
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
        if city is not None:
            query_sql = sql_pattern.sql_select_city
            query_arg = [city]
        elif posName is not None:
            query_sql = sql_pattern.sql_select_pos
            query_arg = [posName]
        else:
            query_sql = sql_pattern.sql_select_pos_city
            query_arg = (posName, city)
        try:
            sql_handler.curs.execute(query_sql, query_arg)
            result = sql_handler.curs.fetchall()
        except Exception as e:
            logging.error("mysql error:", exc_info=True)
            return False, result
        return True, result

    def get_data_default(self):
        pass


if __name__ == '__main__':
    pass
