#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: satrt_ad.py
Author: cwk
Date: 4/12/18
"""


import logging
import os
import platform
import signal
import sys
import time

sys.path.append('../')
from lib import log
import environment
import src.application as http_ad
from src.biz import db_util


SLEEP_INTERVAL = 30
PID_DICT = {}
MODULE_NAME = "daVinci"


def stop_handler(signum, frame):
    """ stop_handler """
    logging.info("Shutdown ad http service.")
    for pid in PID_DICT.keys():
        os.kill(pid, signal.SIGTERM)


def start_server(self_hostid):
    """ start_server """
    try:
        signal.signal(signal.SIGTERM, http_ad.stop_http)
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        signal.signal(signal.SIGUSR1, signal.SIG_IGN)

        db_factory = db_util.DbHandlerFactory()
        logging.info("begin start_server, host_index: %s" % self_hostid)
        http_ad.start_http('HTTP_LUNA',
                               self_hostid,
                               environment.http_config,
                               environment.ad_biz_conf,
                               db_factory)
        os._exit(0)
    except Exception as e:
        logging.error("unknown error! %s" % str(e), exc_info=True)
        os._exit(1)


def setup_log_for_instance(service_name, instance_no):
    """ setup_log_for_instance """
    log_name = '%s-%s-%s-%s' % (platform.node(), MODULE_NAME, service_name, instance_no)

    log.init_log(log_path='/home/dk/code/log/ad_main',
                 log_name=log_name,
                 level=environment.log_config["level"],
                 test=environment.http_config['test'])

    logging.info("set up log for instance[%s]" % instance_no)


def http_process(service_name):
    """the main process for http"""
    logging.info("http server start")

    for hid in environment.http_config['start_hostids']:
        pid = os.fork()

        if pid == 0:
            setup_log_for_instance(service_name, hid)
            start_server(hid)
            return
        else:
            PID_DICT[pid] = hid
            logging.info("create instace[%s]" % hid)

    signal.signal(signal.SIGTERM, stop_handler)
    signal.signal(signal.SIGINT, stop_handler)
    signal.signal(signal.SIGUSR1, signal.SIG_IGN)
    signal.signal(signal.SIGUSR2, signal.SIG_IGN)

    while PID_DICT:
        try:
            pid, ret = os.wait()
            logging.info('the ret: %d, the sys.argv %s' % (ret, sys.argv))

            hid = PID_DICT[pid]
            del PID_DICT[pid]

            if ret > 0:
                logging.error("luna http process %d died accidentally!", hid)
                if len(sys.argv) > 1:
                    time.sleep(SLEEP_INTERVAL)

                    pid = os.fork()
                    if pid != 0:
                        # parent process
                        PID_DICT[pid] = hid
                    else:
                        # child process
                        setup_log_for_instance(service_name, hid)
                        start_server(hid)
        except Exception as e:
            print "catch exception in start_http_luna main, %s" % str(e)
            pass


if __name__ == '__main__':
    environment.main(http_process, 'http_ad')
