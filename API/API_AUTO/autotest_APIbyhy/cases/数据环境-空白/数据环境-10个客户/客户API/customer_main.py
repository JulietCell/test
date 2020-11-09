from hyrobot.common import *
from lib.webAPI import apimgr
import json


class C2():
    name = '添加客户 API-0152'


    #清除方法
    def teardown(self):
        apimgr.del_customer(self.addcustomerId)

    def teststeps(self):

        STEP(1,'先列出客户')
        r = apimgr.list_all_customer()
        customerList1 = r['retlist']

        STEP(2,'添加一个客户')
        addret = apimgr.add_customer('南京市鼓楼医院',
                            '13345679934',
                            "南京市鼓楼北路")
        self.addcustomerId = addret['id']

        CHECK_POINT('检查返回的ret值',r['ret'] == 0)

        STEP(3,'再次列出客户')
        retlist = apimgr.list_all_customer('11')

        expected = {
                        "ret": 0,
                        "retlist": [
                            {
                                "address": "南京市鼓楼北路",
                                "id": addret['id'],
                                "name": "南京市鼓楼医院",
                                "phonenumber": "13345679934"
                            }
                        ] +customerList1,
                        'total': 11
                    }
        CHECK_POINT('返回的消息体数据正确',retlist == expected)