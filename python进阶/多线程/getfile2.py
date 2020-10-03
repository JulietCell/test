import requests
import os
from time import sleep
from threading import Thread,Lock
taskList = [
    'http://mirrors.163.com/centos/6/isos/x86_64/README.txt',
    'http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt',
    'http://mirrors.kernel.org/gnu/gnome.README',
]
readme89old = {}
readmelock = Lock()
def requestAndGet(threadidx,url):
    # readmelock.acquire()
    res = requests.get(url)
    sleep(0.1)
    readmelock.acquire()
    readme89old[threadidx] = res.text
    readmelock.release()
threadlist = []
for idx in range(len(taskList)):
    thread = Thread(target=requestAndGet,
                    args=(idx,taskList[idx]))
    thread.start()
    threadlist.append(thread)

for thread in threadlist :
    thread.join()


print('主线程结束')
with open("readme89.txt",'w',encoding="utf-8") as f :
    readme89new = {}
    dict_list = sorted(readme89old.items(),key=lambda x :x[0])
    # for value in dict_list:
    #     readme89new[value[0]]=str(value[1])
    # for k,v in readme89new.items():
    #     f.write(v)        #避开字典无序性
    for value in dict_list:
        f.write(value[1])