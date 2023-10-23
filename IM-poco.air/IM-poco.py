# -*- encoding=utf8 -*-
__author__ = "huangchaoyang3"

from airtest.core.api import *

auto_setup(__file__)


from airtest.core.api import *
from poco.drivers.ios import iosPoco
poco = iosPoco()
auto_setup(__file__)
# 启动微信
touch(Template(r"tpl1697873017449.png", record_pos=(0.118, 0.915), resolution=(1170, 2532)))

assert_exists(Template(r"tpl1697873052586.png", record_pos=(-0.372, 0.936), resolution=(1170, 2532)), "验证是否存在微信模块")

poco("发现").click()
poco("朋友圈").click()
screenWidth,screenHeigth = poco.get_screen_size()
while True:
    #查找评论按钮
#     tableList = poco("Table").child('Cell').offspring('评论')
    tableList = touch(Template(r"tpl1697874056167.png", record_pos=(0.403, 0.817), resolution=(1170, 2532)))

    #点击评论按钮
    for child in tableList:
        childX,childY = child.get_position()
        print(childX)
        print(childY)
        if (childY>=0.1 and childY<1.0):
            child.click()
            if poco("赞").exists():
                touch(Template(r"tpl1697873455228.png", record_pos=(-0.009, 0.834), resolution=(1170, 2532)))
        # poco("赞").click()

 #向上滑动一个屏幕的高度
    swipe((screenWidth*0.5,screenHeigth*0.9),vector=[0,-0.8],duration=2.5)
    #等滚动动画结束
    sleep(5)