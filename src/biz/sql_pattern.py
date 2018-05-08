#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: sql_pattern.py
Author: cwk
Date: 4/19/18
"""

sql_select_pos_city = """
                  SELECT a.ad_id, a.companyName, a.positionfullName, a.positionName, a.city, a.positionAdvantage, a.salarymin, a.salarymax, a.workYear, a.request_url, a.record_url, a.priority 
                      FROM ad_info as a, tbl_cpc_clk as c
                      WHERE a.clk_id=c.clk_id 
                      AND c.num<50
                      AND c.date=%s
                      AND a.positionName=%s
                      AND a.city=%s
                      AND a.stime<=%s
                      AND a.etime>=%s
                  ORDER BY a.priority
                  LIMIT 30
"""

sql_select_pos = """
                  SELECT a.ad_id, a.companyName, a.positionfullName, a.positionName, a.city, a.positionAdvantage, a.salarymin, a.salarymax, a.workYear, a.request_url, a.record_url, a.priority 
                      FROM ad_info as a, tbl_cpc_clk as c, tbl_tariff as t
                      WHERE a.clk_id=c.clk_id 
                      AND t.ad_id=a.ad_id
                      AND a.ad_id=c.ad_id
                      AND c.num<50
                      AND c.date=%s
                      AND a.positionName=%s
                      AND a.stime<=%s
                      AND a.etime>=%s
                      AND t.balance>0
                  ORDER BY a.priority
                  LIMIT 30
"""

sql_select_city = """
                  SELECT a.ad_id, a.companyName, a.positionfullName, a.positionName, a.city, a.positionAdvantage, a.salarymin, a.salarymax, a.workYear, a.request_url, a.record_url, a.priority 
                      FROM ad_info as a, tbl_cpc_clk as c
                      WHERE a.clk_id=c.clk_id 
                      AND c.num<50
                      AND c.date=%s
                      AND a.city=%s
                      AND a.stime<=%s
                      AND a.etime>=%s
                  ORDER BY a.priority
                  LIMIT 30
"""

sql_insert_ad_data = """
                    INSERT INTO ad_info (companyName, positionfullName, positionName, city, positionAdvantage, salarymin, salarymax, workYear, request_url, record_url, priority, clk_id, stime, etime)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

get_next_primary_key = """select auto_increment from information_schema.`TABLES` 
                          where table_name=%s 
                          and TABLE_SCHEMA=%s
"""

sql_insert_cpc_data = """
                       INSERT INTO tbl_tariff (ad_id, stored, balance, cpc_spend)
                       VALUES (%s, %s, %s, %s)
"""

sql_update_cpc_num = """
                    UPDATE tbl_cpc_clk SET num=(num + 1)
                    WHERE clk_id=%s
                    AND date=%s
                    AND ad_id=%s
"""

sq_update_cpc_balance = """
                    UPDATE tbl_tariff SET balance=(balance-cpc_spend)
                    WHERE ad_id=%s
"""

sql_select_cpc = """
                 SELECT num, date FROM tbl_cpc_clk 
                 WHERE ad_id=%s
"""

sql_select_ban = """
                SELECT balance FROM tbl_tariff
                WHERE ad_id=%s
"""
