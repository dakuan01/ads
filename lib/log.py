#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: log.py
Author: cwk
Date: 4/11/18
"""

import curses
import logging
import logging.handlers
import os
import sys
import time


class LogFormatter(logging.Formatter):
    """ brief info for: LogFormatter
            custom format for log
    """

    def __init__(self, format, color, service):
        """ init sth"""
        logging.Formatter.__init__(self)
        self._format = format
        self._color = color
        self.service = service

        if color:
            fg_color = curses.tigetstr("setaf") or curses.tigetstr("setf") or ""
            self._colors = {
                logging.DEBUG: curses.tparm(fg_color, 4),  # Blue
                logging.INFO: curses.tparm(fg_color, 2),  # Green
                logging.WARNING: curses.tparm(fg_color, 3),  # Yellow
                logging.ERROR: curses.tparm(fg_color, 1),  # Red
            }
            self._normal = curses.tigetstr("sgr0")

    def format(self, record):
        """ format """
        try:
            record.message = record.getMessage()
        except Exception, e:
            record.message = "Bad message (%r): %r" % (e, record.__dict__)

        record.asctime = time.strftime("%y%m%d %H:%M:%S", self.converter(record.created))
        record.service = self.service

        prefix = self._format % record.__dict__

        if self._color:
            prefix = (self._colors.get(record.levelno, self._normal) + prefix + self._normal)
        formatted = "%s %s" % (prefix, record.message)

        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            formatted = formatted.rstrip() + "\n" + record.exc_text
        return formatted.replace("\n", "\n    ")


def init_log(log_path=None, log_name=None, level="INFO", backup=7, max_bytes=50 * 1024 * 1024,
             format="[%(levelname)1.1s %(asctime)s %(service)s %(module)s:%(lineno)d]", test=True):
    """
    init_log - initialize log module
    Args:
        log_path    - Log file path prefix.
                      Log data will go to two files: log_path.log and log_path.log.wf
                      Any non-exist parent directories will be created automatically
        log_name    - log_name
        level       - msg above the level will be displayed
                      DEBUG < INFO < WARNING < ERROR < CRITICAL
                      the default value is logging.INFO
        max_bytes   - split log by volume, max_bytes is the volume of evry log
        format      - format of the log
                      default format:
                      %(levelname)s: %(asctime)s: %(filename)s:%(lineno)d * %(thread)d %(message)s
                      INFO: 12-09 18:02:42: log.py:40 * 139814749787872 HELLO WORLD
        backup      - how many backup file to keep
                      default value: 7
        test        - True is test, False is online
    Raises:
        OSError: fail to create log directories
        IOError: fail to open log file
    """
    assert log_path
    assert log_name

    logger = logging.getLogger(log_name)
    logger.setLevel(getattr(logging, level))

    dir = os.path.dirname(log_path)
    if not os.path.isdir(dir):
        os.makedirs(dir)

    # generate file handler
    handler = logging.handlers.TimedRotatingFileHandler(log_path + ".log", encoding="utf-8")
    handler.setFormatter(LogFormatter(format=format, color=False, service=log_name))
    handler.setLevel(level)
    logger.addHandler(handler)

    # generate std handler
    color = False
    if curses and sys.stderr.isatty():
        try:
            curses.setupterm()
            if curses.tigetnum("colors") > 0:
                color = True
        except Exception as e:
            print "catch exception when generate std log handler"
            pass

    # open StreamHandler when test
    if test:
        handler = logging.StreamHandler()
        handler.setFormatter(LogFormatter(format=format, color=color, service=log_name))
        logger.addHandler(handler)

    logging.debug = logger.debug
    logging.info = logger.info
    logging.warning = logger.warning
    logging.error = logger.error
    logging.critical = logger.critical
    logging.logger = logger
