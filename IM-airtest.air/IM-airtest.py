# -*- encoding=utf8 -*-
__author__ = "huangchaoyang3"

from airtest.core.api import *

auto_setup(__file__)
touch(Template(r"tpl1697868929444.png", record_pos=(-0.117, 0.219), resolution=(1170, 2532)))
assert_exists(Template(r"tpl1697868993525.png", record_pos=(0.003, 0.231), resolution=(1170, 2532)), "验证刷脸登录按钮是否存在")
touch(Template(r"tpl1697869022224.png", record_pos=(0.008, 0.512), resolution=(1170, 2532)))
touch(Template(r"tpl1697869031380.png", record_pos=(-0.221, -0.21), resolution=(1170, 2532)))
text("18728421687")
touch(Template(r"tpl1697869054937.png", record_pos=(-0.23, -0.039), resolution=(1170, 2532)))
text("12345678a.")
touch(Template(r"tpl1697870438463.png", record_pos=(0.397, 0.159), resolution=(1170, 2532)))

touch(Template(r"tpl1697869113948.png", record_pos=(0.003, 0.237), resolution=(1170, 2532)))

assert_exists(Template(r"tpl1697869157914.png", record_pos=(-0.009, -0.006), resolution=(1170, 2532)), "验证点击登录后，是否弹出隐私申明提示框")
touch(Template(r"tpl1697869223664.png", record_pos=(0.199, 0.176), resolution=(1170, 2532)))

touch(Template(r"tpl1697869236992.png", record_pos=(0.008, 0.237), resolution=(1170, 2532)))
assert_exists(Template(r"tpl1697869273200.png", record_pos=(-0.402, 0.941), resolution=(1170, 2532)), "验证是否存在消息模块")
text("登录成功")


