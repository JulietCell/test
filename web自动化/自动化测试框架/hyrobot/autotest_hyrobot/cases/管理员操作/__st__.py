from hyrobot.common import *
from lib.webui import *

def suite_setup():
    INFO('suite_setup')
    wd = open_browser()
    mgr_login(wd)

def suite_teardown():
    INFO('suite_teardown')
    print('清除添加的所有客户，药品，和订单')
    wd = get_lobal_webdriver()
    #清除添加的所有客户，药品，和订单
    clear_all_message(wd)
    wd.quit()