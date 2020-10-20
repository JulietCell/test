import requests,json
from fiddler_customer import customerId
from fiddler_medicine import medicineId

#设置代理
proxies = {
    'http':'http://127.0.0.1:8888',
    'https':'http://127.0.0.1:8888'
}

#打印响应信息
def printResponse(response):
    print('\n\n-------- HTTP response * begin -------')
    print(response.status_code)

    for k, v in response.headers.items():
        print(f'{k}: {v}')

    print('')

    print(response.json())    #为了方便处理 可以把响应消息中json格式的数据转化为python中的数据对象
    # print(response.content.decode('utf8'))    #json格式的数据对象
    print('-------- HTTP response * end -------\n\n')

#创建session对象
session = requests.Session()

#登录
def login():
    #请求消息体
    body = {'username':'byhy','password':'88888888'}

    response = session.post('http://127.0.0.1/api/mgr/signin',data=body,proxies=proxies)
    printResponse(response)

#列出所有订单
def list_all_order():
    login()
    #请求URL参数
    params = {
        'action':'list_order',
        'pagesize':'5',
        'pagenum':'1',
        'keywords':''
    }

    response = session.get('http://127.0.0.1/api/mgr/orders',proxies=proxies,params=params)
    printResponse(response)

#添加一个订单
def add_order(customerId,medicineId):
    login()
    #请求消息体
    body = {
    "action":"add_order",
    "data":{
        "name":"华山医院订单002",
        "customerid":customerId,
        "medicinelist":[
            {"id":medicineId,"amount":5,"name":"环丙沙星"},
        ]
    }
}
    response = session.post('http://127.0.0.1/api/mgr/orders',json=body)
    printResponse(response)

#删除订单

def del_order(id):
    login()
    # 请求消息体
    body = {
    "action":"delete_order",
    "id": id
}
    response = session.post('http://127.0.0.1/api/mgr/orders', json=body)
    printResponse(response)


# login()
#list_all_order()
add_order(customerId,medicineId)
#modify_order(123)
#del_order(23)
#list_all_order()
