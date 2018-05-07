#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: cpc_clk_handler.py
Author: cwk
Date: 5/2/18
"""

import os
import logging

from src.biz.base_handler import BaseHandler


result = """
<html>
<head>
<script>
window.back()
</script>
</head>
</html>
"""



class CpcClkHandler(BaseHandler):

    def get(self):

        positionId = self.get_argument('positionId')
        logging.debug('position id is %s' % positionId)

        self.write(result)


if __name__ == '__main__':
    print "no process in __main__, %s" % os.path.realpath(__file__)
