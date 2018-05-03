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
                      FROM ad_info as a, tbl_cpc_clk as c
                      WHERE a.clk_id=c.clk_id 
                      AND c.num<50
                      AND c.date=%s
                      AND a.positionName=%s
                      AND a.stime<=%s
                      AND a.etime>=%s
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