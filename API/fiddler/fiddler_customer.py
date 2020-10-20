import requests,json

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

    responseJson = response.json()
    print(responseJson)    #为了方便处理 可以把响应消息中json格式的数据转化为python中的数据对象
    # print(response.content.decode('utf8'))    #json格式的数据对象
    print('-------- HTTP response * end -------\n\n')

    return responseJson

#创建session对象
session = requests.Session()

#登录
def login():
    #请求消息体
    body = {'username':'byhy','password':'88888888'}

    response = session.post('http://127.0.0.1/api/mgr/signin',data=body,proxies=proxies)
    printResponse(response)

#列出所有客户
def list_all_customer():
    login()
    #请求URL参数
    params = {
        'action':'list_customer',
        'pagesize':'5',
        'pagenum':'1',
        'keywords':''
    }

    response = session.get('http://127.0.0.1/api/mgr/customers',proxies=proxies,params=params)
    printResponse(response)

#添加一个客户
def add_customer():
    login()
    #请求消息体
    body = {
    "action":"add_customer",
    "data":{
        "name":"武汉市桥西医院",
        "phonenumber":"13345679934",
        "address":"武汉市桥西医院北路"
    }
}
    response = session.post('http://127.0.0.1/api/mgr/customers',json=body)
    responseJson = printResponse(response)

    return responseJson['id']

#修改客户信息
def modify_customer(id):
    login()
    # 请求消息体
    body = {
    "action":"modify_customer",
    "id": id,
    "newdata":{
        "name":"武汉市桥北医院",
        "phonenumber":"13345678888",
        "address":"武汉市桥北医院北路"
    }
}
    response = session.post('http://127.0.0.1/api/mgr/customers', json=body)
    printResponse(response)

#删除客户
def del_customer(id):
    login()
    # 请求消息体
    body = {
    "action":"del_customer",
    "id": id
}
    response = session.post('http://127.0.0.1/api/mgr/customers', json=body)
    printResponse(response)


# login()
#list_all_customer()
customerId =add_customer()
# #modify_customer(145)
#del_customer(146)
#list_all_customer()