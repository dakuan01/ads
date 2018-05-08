#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: __init__.py.py
Author: cwk
Date: 5/2/18
"""

import MySQLdb
import time
import random

sql_select = """
             SELECT ad_id, clk_id from ad_info
"""

sql_insert = """
             replace INTO tbl_cpc_clk (ad_id, num, date, clk_id)
             VALUES (%s, %s, %s, %s)
"""


def gettestdata():
    sql_conn = MySQLdb.connect(host='localhost', user='root', db='test', passwd='h', charset='utf8')
    sql_curs = sql_conn.cursor()
    sql_curs.execute(sql_select)
    rows = sql_curs.fetchall()
    date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    print type(date)
    for row in rows:
        num = random.randint(0, 100)
        try:
            sql_curs.execute(sql_insert, (row[0], num, date, row[1]))
        except Exception as e:
            sql_conn.rollback()
            print str(e)
    sql_conn.commit()
    sql_conn.close()


def main():
    gettestdata()


if __name__ == '__main__':
    main()
