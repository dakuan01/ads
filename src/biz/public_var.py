#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: public_var.py
Author: cwk
Date: 4/19/18
"""

HTTP_OK = 200
RESULT_CODE_SUC = 2000
RESULT_CODE_FAILED = 5000

FAILED_MYSQL_QUERY = 5001
WRONG_FORMAT = 5002
FAILED_MYSQL_INSERT = 5003

city_list = {'深圳', '西安', '北京', '上海'}
job_list = {'c', 'c++', 'python', 'java', '数据挖掘', 'C', 'C++', 'Python', 'Java'}

ERROR_MESSAGE = {
    FAILED_MYSQL_QUERY: u'5001查询数据库失败',
    WRONG_FORMAT: u'5002输入参数格式有误',
    FAILED_MYSQL_INSERT: u'5003插入数据失败，添加广告失败'
}
