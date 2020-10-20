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

#列出所有药品
def list_all_medicine():
    login()
    #请求URL参数
    params = {
        'action':'list_medicine',
        'pagesize':'5',
        'pagenum':'1',
        'keywords':''
    }

    response = session.get('http://127.0.0.1/api/mgr/medicines',proxies=proxies,params=params)
    printResponse(response)

#添加一个药品
def add_medicine():
    login()
    #请求消息体
    body = {
    "action":"add_medicine",
    "data":{
        "name": "青霉素",
        "desc": "青霉素 国字号",
        "sn": "099877883837"
    }
}
    response = session.post('http://127.0.0.1/api/mgr/medicines',json=body)
    responseJson = printResponse(response)
    return responseJson['id']

#修改药品信息
def modify_medicine(id):
    login()
    # 请求消息体
    body = {
    "action":"modify_medicine",
    "id": id,
    "newdata":{
        "name": "青黄霉素",
        "desc": "青黄霉素 国字号",
        "sn": "099877883839"
    }
}
    response = session.post('http://127.0.0.1/api/mgr/medicines', json=body)
    printResponse(response)

#删除药品
def del_medicine(id):
    login()
    # 请求消息体
    body = {
    "action":"del_medicine",
    "id": id
}
    response = session.post('http://127.0.0.1/api/mgr/medicines', json=body)
    printResponse(response)


# login()
#list_all_medicine()
medicineId = add_medicine()
#modify_medicine(123)
#del_medicine(122)
#list_all_medicine()
