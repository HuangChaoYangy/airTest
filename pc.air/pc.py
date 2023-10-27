# -*- encoding=utf8 -*-
__author__ = "huangchaoyang3"

from airtest.core.api import *

auto_setup(__file__)
if exists(Template(r"tpl1698138363050.png", threshold=1.0, record_pos=(0.193, -0.064), resolution=(3286, 1080))):
    print('pass')
else:
    print('no pass')
