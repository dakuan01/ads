#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: main.py
Author: cwk
Date: 4/13/18
"""

import logging
import json
from src.biz import sql_pattern
from src.biz.base_handler import BaseHandler
from src.biz import http_util


main_page = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>广告</title>
</head>

<form action="/ad_re" method="GET">
info:<br>
<input type="text" name="info">
<br><br>
<input type="submit" value="搜索">
</form>
<body>

</body>
</html>
"""


class MainHandler(BaseHandler):
    """主页"""

    def prepare(self):
        """
        设置数据交互格式
        :return:
        """
        self.content_type = 'html'

    def get(self):

        self.write(main_page)



