from hyrobot.common import *
from lib.webAPI import apimgr
import json
import random

class C1():
    name = '添加客户 API-0151'

    #清除方法
    def teardown(self):
        apimgr.del_customer(self.customerId)

    def teststeps(self):

        STEP(1,'添加一个客户')
        addret = apimgr.add_customer('武汉市桥西医院',
                            '13345679934',
                            "武汉市桥西医院北路")

        self.customerId = addret['id']

        CHECK_POINT('返回的ret值为0',addret['ret'] == 0)

        STEP(2,'检查系统数据')
        list_all_ret = apimgr.list_all_customer()
        expected = {
                        "ret": 0,
                        "retlist": [
                            {
                                "address": "武汉市桥西医院北路",
                                "id": addret['id'],
                                "name": "武汉市桥西医院",
                                "phonenumber": "13345679934"
                            }
                        ] ,
                        'total': 1
                    }
        CHECK_POINT('返回的消息体数据正确',list_all_ret == expected)

class C3():
    name = '添加客户 API-0153'

    def teststeps(self):
        STEP(1,'添加客户，使客户名字段缺失')

        body = {
        "action":"add_customer",
        "data":{
            "phonenumber":'13345679934',
            "address":"武汉市桥西医院北路"
               }
               }
        r = apimgr.usebody_add_customer(body)

        CHECK_POINT('返回的ret',
                    r == {
                        "ret": 1,
                        "msg": "请求消息参数错误"
                        })

        STEP(2,'检查系统数据')

        r = apimgr.list_all_customer()

        CHECK_POINT('返回的ret',
                    r == {
                        "ret": 0,
                        "retlist": [],
                        'total': 0
                        }
                        )

class C4():
    name = '修改客户 API-0201'

    def teststeps(self):

        STEP(1,'当没有客户的情况下，修改一个客户，并且此客户ID不存在')

        ret = apimgr.modify_customer(random.randint(1,500))

        STEP(2,'检查ret')
        expected = {
                        "ret": 1,
                        "msg":  "客户ID不存在",
                    }

        CHECK_POINT('检查ret是否符合预期',ret == expected)

class C5():
    name = '修改客户 API-0202'

    #初始化，添加一个用户
    def setup(self):
        ret = apimgr.add_customer('武汉市桥西医院',
                            '13345679934',
                            "武汉市桥西医院北路")
        self.cid = ret['id']
        self.name = '武汉市桥西医院'
        self.phoneNum = '13345679934'
        self.adress = "武汉市桥西医院北路"

    #清除
    def teardown(self):
        apimgr.del_customer(self.cid)

    def teststeps(self):

        STEP(1,'修改客户，只修改电话号码')
        ret = apimgr.modify_customer(self.cid,self.name,'11111111111',self.adress)

        STEP(2,'检查ret')

        expected = {
                        "ret": 0
                    }

        CHECK_POINT('ret的返是否回正确',ret == expected)

class C6():
    name = '修改客户 API-0203'

    #初始化，添加一个用户
    def setup(self):
        ret = apimgr.add_customer('武汉市桥西医院',
                            '13345679934',
                            "武汉市桥西医院北路")
        self.cid = ret['id']
        self.name = '武汉市桥西医院'
        self.phoneNum = '13345679934'
        self.adress = "武汉市桥西医院北路"

    #清除
    def teardown(self):
        apimgr.del_customer(self.cid)

    def teststeps(self):

        STEP(1,'修改客户，只修改地址')
        ret = apimgr.modify_customer(self.cid,self.name,self.phoneNum,'武汉市某某地')

        STEP(2,'检查ret')

        expected = {
                        "ret": 0
                    }

        CHECK_POINT('ret的返是否回正确',ret == expected)

class C7():
    name = '删除客户 API-0251'

    def teststeps(self):

        STEP(1,'删除一个ID不存在的客户')
        ret = apimgr.del_customer(random.randint(1,500))

        expected = {
                        "ret": 1,
                        "msg":  "客户ID不存在",
                    }

        CHECK_POINT('ret的信息是否正确',ret == expected)

        STEP(2,'检查系统数据')
        ret = apimgr.list_all_customer()
        CHECK_POINT('检查ret返回',ret == {
                        "ret": 0,
                        "retlist": [],
                        'total': 0
                        }
                        )

class C8():
    name = '删除客户 API-0252'

    #初始化，添加一个客户
    def setup(self):
        ret = apimgr.add_customer('武汉市桥西医院',
                            '13345679934',
                            "武汉市桥西医院北路")

        self.cid = ret['id']


    def teststeps(self):
        STEP(1,'删除添加的用户')
        ret = apimgr.del_customer(self.cid)
        CHECK_POINT('检查ret返回',ret == { "ret": 0 })

        STEP(2,'检查系统数据')
        ret = apimgr.list_all_customer()
        CHECK_POINT('检查ret返回',ret == {
                        "ret": 0,
                        "retlist": [],
                        'total': 0
                        }
                        )








