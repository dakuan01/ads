#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: add_new_ad_handler.py
Author: cwk
Date: 5/6/18
"""

import logging
import time
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
        pass

    def get_param_argument(self):
        """
        获取请求参数
        :return:
        """
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


if __name__ == '__main__':
    print "no process in __main__, %s" % os.path.realpath(__file__)
