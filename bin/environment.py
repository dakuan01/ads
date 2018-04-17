#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: environment.py
Author: cwk
Date: 4/11/18
"""

import logging
import commands
import os
import sys
import signal

sys.path.append('../')

from lib import log

BIN_PATH = os.path.dirname(os.path.realpath(__file__))
WORK_ROOT = os.path.split(BIN_PATH)[0]
CONF_PATH = os.path.join(WORK_ROOT, "conf")
SERVICE_CONF_PATH = os.path.join(WORK_ROOT, "src/conf/")
LIB_PATH = os.path.join(WORK_ROOT, 'lib')
SERVICE_PY_PATH = os.path.join(WORK_ROOT, 'src')


python_path = LIB_PATH
python_path += (':' + SERVICE_PY_PATH)

org_python_path = os.getenv('PYTHONPATH')
if org_python_path is not None:
    python_path += (':' + org_python_path)
os.environ['PYTHONPATH'] = python_path

print '-' * 100
print "PYTHONPATH:\n" + "\n".join(python_path.split(':'))
print '-' * 100

http_config = {}
http_config_path = os.path.join(CONF_PATH, 'http.conf')
execfile(http_config_path)

log_config = {}
log_config_path = os.path.join(CONF_PATH, "log.conf")
print log_config_path
execfile(log_config_path, log_config)

ad_biz_conf = {}
ad_biz_conf_path = os.path.join(SERVICE_CONF_PATH, 'ad_biz_conf')


def main():
    """
    将日志管理字段添加进系统
    :return:
    """
    log.init_log(log_path='/home/dk/code/log/ad_main', log_name='ad_main', level=log_config["level"],
                 test=http_config['test'])
    logging.info("init  log")


if __name__ == '__main__':
    main()
