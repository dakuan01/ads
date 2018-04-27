#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: sql_pattern.py
Author: cwk
Date: 4/19/18
"""

sql_select_pos_city = """
                  SELECT * FROM ad_info 
                  WHERE positionName=%s
                  AND city=%s
"""

sql_select_pos = """
                 SELECT * FROM ad_info
                 WHERE positionName=%s
"""

sql_select_city = """
                  SELECT * FROM ad_info
                  WHERE city=%s
"""