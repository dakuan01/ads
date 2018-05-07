#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: main.py
Author: cwk
Date: 4/13/18
"""

import logging
import os
import json
from src.biz import sql_pattern
from src.biz.base_handler import BaseHandler
from src.biz import http_util
from src.biz import public_var


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

test_page = """
<html>
<head>
<SCRIPT LANGUAGE="JavaScript">
function adClick(ad, site) {
window.open(ad);
window.location = site;}
</script>
</head>
<body>
<a href="javascript:adClick('https://www.lagou.com/jobs/3022338.html', '/cpc_clk');">名称</a>
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

        # template_vars = {
        #     'title': u'招聘信息',
        #     'ads': ads
        # }
        # self.make_return(public_var.HTTP_OK, template_vars, 'ok', 'main.html')
        self.write(main_page)


if __name__ == '__main__':
    print "no process in __main__, %s" % os.path.realpath(__file__)
