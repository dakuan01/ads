#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: ad_ recommend_handler.py
Author: cwk
Date: 4/26/18
"""

import logging
import json
import os
from src.biz.base_handler import BaseHandler
from src.biz import public_var
from src.biz import http_util


class AdRecommendHandler(BaseHandler):

    def prepare(self):
        """
        设置数据交互格式
        :return:
        """

    def get(self):
        """
        返回广告结果
        :return:
        """

        param_dict = self.get_url_request_info()
        logging.debug('param is :%s' % str(param_dict))
        result = list()
        ret_data = dict()
        if param_dict['city'] is not None or param_dict['posName'] is not None:
            falg, result = self.get_data_param(param_dict)
        elif param_dict['info'] is not None:
            falg, result = self.get_data_search(param_dict)
        else:
            falg, result = self.get_data_default()
        logging.info('flag is %s' % str(falg))

        if falg:
            ret_data['code'] = public_var.RESULT_CODE_SUC
            ret_data['msg'] = 'OK'
            ret_data['ads'] = result
        else:
            ret_data['code'] = public_var.FAILED_MYSQL_QUERY
            ret_data['msg'] = public_var.ERROR_MESSAGE[public_var.FAILED_MYSQL_QUERY]

        self.write(json.dumps(ret_data, ensure_ascii=False))

    def get_url_request_info(self):
        """
        获取请求数据
        :return:
        """

        param_dict = dict()
        param_dict['city'] = self.get_argument('city', None)
        param_dict['posName'] = self.get_argument('posName', None)
        param_dict['info'] = self.get_argument('info', None)
        return param_dict


if __name__ == '__main__':
    print "no process in __main__, %s" % os.path.realpath(__file__)
