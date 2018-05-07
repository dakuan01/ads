#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: jinja_base_handler.py
Author: cwk
Date: 5/3/18
"""

import os
import logging

import jinja2
from tornado.web import RequestHandler


class TemplateRendering(object):
    """ TemplateRendering """

    def render_template(self, env, template_name, **kwargs):
        try:
            template = env.get_template(template_name)
            logging.debug("template is %s" % str(template))
        except jinja2.TemplateNotFound:
            raise jinja2.TemplateNotFound(template_name)
        content = template.render(kwargs)
        logging.debug('content is %s' % str(content))
        return content


class JinjaBaseHandler(RequestHandler, TemplateRendering):
    """ JinjaBaseHandler """

    def render2(self, template_name, **kwargs):
        logging.debug("JinjaBaseHandler render2 : ssssssssssssssss")
        content = self.render_template(self.application.jinja_env, template_name, **kwargs)
        self.write(content)


if __name__ == "__main__":
    print "no process in __main__, %s" % os.path.realpath(__file__)
