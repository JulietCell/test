from hyrobot.common import *
from lib.webAPI import apimgr

#初始化方法
def suite_setup():
    INFO('删除订单、客户、药品')
    apimgr.mgr_login(useProxy=True)
    apimgr.del_all_order()
    apimgr.del_all_medicine()
    apimgr.del_all_customer()