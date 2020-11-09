from hyrobot.common import *
from lib.webAPI import apimgr

suite_data_customerids = []
#初始化方法
def suite_setup():
    global suite_data_customerids
    INFO('添加10个客户')
    for i in range(10):
        r = apimgr.add_customer(f'武汉市桥西医院_{i + 1}',
                                f'13345679934{i + 1:02d}',
                                f'武汉市桥西医院北路_{i + 1}')
        suite_data_customerids.append(r['id'])

def suite_teardown():
    global suite_data_customerids
    for cid in suite_data_customerids:
        apimgr.del_customer(cid)