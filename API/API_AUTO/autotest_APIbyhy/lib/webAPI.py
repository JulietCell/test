import requests
from cfg import cfg
from pprint import pprint
import json

#定义类
class APIMgr():

    #打印信息
    def _printResponse(self,response):
        print('\n\n-------- HTTP response * begin -------')
        print(response.status_code)

        for k, v in response.headers.items():
            print(f'{k}: {v}')

        print('')

        responseJsonToPython = response.json()
        print(responseJsonToPython)  # 为了方便处理 可以把响应消息中json格式的数据转化为python中的数据对象
        print('-------- HTTP response * end -------\n\n')
        return responseJsonToPython

    #登录
    def mgr_login(self,username='byhy',password='88888888',useProxy=False):
        self.session = requests.Session()

        # 如果使用代理，则设置代理
        if useProxy:
            self.session.proxies.update({
                                            'http':'http://127.0.0.1:8888',
                                            'https':'http://127.0.0.1:8888'
                                        })
        # 请求消息体
        body = {'username': username, 'password': password}

        response = self.session.post(f'http://{cfg.target_host}/api/mgr/signin', data=body)
        responseJsonToPython = self._printResponse(response)

        return responseJsonToPython


    #客户相关操作
    #列出所有客户
    def list_all_customer(self,pagesize='10',pagenumber='1',keywords=''):
        #请求URL参数
        params = {
            'action':'list_customer',
            'pagesize':pagesize,
            'pagenum':pagenumber,
            'keywords':keywords
        }

        response = self.session.get(f'http://{cfg.target_host}/api/mgr/customers',params=params)
        responseJsonToPython = self._printResponse(response)

        return responseJsonToPython


    #添加客户
    def add_customer(self,name,phonenumber,address):
        #请求消息体
        body = {
        "action":"add_customer",
        "data":{
            "name":name,
            "phonenumber":phonenumber,
            "address":address
        }
    }
        response = self.session.post(f'http://{cfg.target_host}/api/mgr/customers',json=body)
        responseJsonToPython = self._printResponse(response)

        return responseJsonToPython

    #修改客户
    def modify_customer(self,cid,
                        name='武汉市桥北医院',
                        phonenumber='13345678888',
                        address='武汉市桥北医院北路'):
        # 请求消息体
        body = {
            "action": "modify_customer",
            "id": cid,
            "newdata": {
                "name": name,
                "phonenumber": phonenumber,
                "address": address
            }
        }
        response = self.session.post(f'http://{cfg.target_host}/api/mgr/customers', json=body)
        responseJsonToPython = self._printResponse(response)

        return responseJsonToPython

    #删除客户
    def del_customer(self,cid):
        # 请求消息体
        body = {
            "action": "del_customer",
            "id": cid
        }
        response = self.session.post(f'http://{cfg.target_host}/api/mgr/customers', json=body)
        responseJsonToPython = self._printResponse(response)

        return responseJsonToPython

    #清除所有客户
    def del_all_customer(self):
        response = self.list_all_customer('100','1')    #整个比较大的数
        theList = response["retlist"]
        for one in theList:
            cid = one['id']
            self.del_customer(cid)

    #自定义消息体添加客户信息
    def usebody_add_customer(self,body):
        response = self.session.post(f'http://{cfg.target_host}/api/mgr/customers', json=body)
        responseJsonToPython = self._printResponse(response)

        return responseJsonToPython

    #自定义消息体修改客户信息
    def usebody_modify_customer(self,body):
        response = self.session.post(f'http://{cfg.target_host}/api/mgr/customers', json=body)
        responseJsonToPython = self._printResponse(response)

        return responseJsonToPython



    #药品相关操作
    # 列出所有药品
    def list_all_medicine(self,pagesize='10',pagenumber='1',keywords=''):
        # 请求URL参数
        params = {
            'action': 'list_medicine',
            'pagesize': pagesize,
            'pagenum': pagenumber,
            'keywords': keywords
        }

        response = self.session.get(f'http://{cfg.target_host}/api/mgr/medicines',params=params)
        responseJsonToPython = self._printResponse(response)

        return responseJsonToPython

    # 添加一个药品
    def add_medicine(self,name,desc,sn):
        # 请求消息体
        body = {
            "action": "add_medicine",
            "data": {
                "name": name,
                "desc": desc,
                "sn": sn
            }
        }
        response = self.session.post(f'http://{cfg.target_host}/api/mgr/medicines', json=body)
        responseJsonToPython = self._printResponse(response)

        return responseJsonToPython

    # 修改药品信息
    def modify_medicine(self,mid,name,desc,sn):
        # 请求消息体
        body = {
            "action": "modify_medicine",
            "id": mid,
            "newdata": {
                "name": name,
                "desc": desc,
                "sn": sn
            }
        }
        response = self.session.post(f'http://{cfg.target_host}/api/mgr/medicines', json=body)
        responseJsonToPython = self._printResponse(response)

        return responseJsonToPython

    # 删除药品
    def del_medicine(self,mid):
        # 请求消息体
        body = {
            "action": "del_medicine",
            "id": mid
        }
        response = self.session.post(f'http://{cfg.target_host}/api/mgr/medicines', json=body)
        responseJsonToPython = self._printResponse(response)

        return responseJsonToPython

    #删除所有药品
    def del_all_medicine(self):
        response = self.list_all_medicine('100','1')
        theList = response['retlist']
        for one in theList:
            mid = one['id']
            self.del_customer(mid)


    #订单操作
    # 列出所有订单
    def list_all_order(self,pagesize='10',pagenumber='1',keywords=''):
        # 请求URL参数
        params = {
            'action': 'list_order',
            'pagesize': pagesize,
            'pagenum': pagenumber,
            'keywords': keywords
        }

        response = self.session.get(f'http://{cfg.target_host}/api/mgr/orders',params=params)
        responseJsonToPython = self._printResponse(response)

        return responseJsonToPython

    # 添加一个订单
    def add_order(self,customerId, medicineId,name,amount):
        # 请求消息体
        body = {
            "action": "add_order",
            "data": {
                "name": name,
                "customerid": customerId,
                "medicinelist": [
                    {"id": medicineId, "amount": amount, "name": "环丙沙星"},
                ]
            }
        }
        response = self.session.post(f'http://{cfg.target_host}/api/mgr/orders', json=body)
        responseJsonToPython = self._printResponse(response)

        return responseJsonToPython


    # 删除订单
    def del_order(self,oid):
        # 请求消息体
        body = {
            "action": "delete_order",
            "id": oid
        }
        response = self.session.post(f'http://{cfg.target_host}/api/mgr/orders', json=body)
        responseJsonToPython = self._printResponse(response)

        return responseJsonToPython

    #删除所有订单
    def del_all_order(self):
        response = self.list_all_order('100', '1')
        theList = response['retlist']
        for one in theList:
            mid = one['id']
            self.del_customer(mid)







apimgr = APIMgr()