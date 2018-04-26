#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: http_util.py
Author: cwk
Date: 4/25/18
"""

import json
import datetime
from decimal import Decimal


class CJsonEncoder(json.JSONEncoder):
    """
    jsonEncoder，用来解决json.dumps报Type error错误，例如针对Decimal、datetime类型
    """

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, Decimal):
            return float(obj)
        else:
            # raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)
            return json.JSONEncoder.default(self, obj)
