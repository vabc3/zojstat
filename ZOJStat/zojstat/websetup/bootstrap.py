# -*- coding: utf-8 -*-
"""Setup the ZOJStat application"""

import logging
from tg import config
from zojstat import model

import transaction


def bootstrap(command, conf, vars):
    """Place any commands to setup zojstat here"""

    # <websetup.bootstrap.before.auth

    # <websetup.bootstrap.after.auth>
