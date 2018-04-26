#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: sql_pattern.py
Author: cwk
Date: 4/19/18
"""

sql_select_test = """
                  SELECT * FROM ad_info 
                  WHERE positionName=%s
                  AND city=%s
"""