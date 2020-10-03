file_name = "D:\\pycharm\\2019-10-22_11.05.40.log"

with open(file_name,"r",encoding="utf-8") as f :
    message = {}
    while True :
        # 按行读，否则文件太大占内存
        contentline = f.readline()
        if len(contentline) ==0 :
            break
        contentline = contentline.strip()
        if not contentline :
            continue
        needinfo = contentline.split("|")[-2]
        if needinfo not in message:
            message[needinfo] = 1
        else:
            message[needinfo] += 1
with open("D:\\pycharm\\chuli.txt","w",encoding="utf-8") as f:
    for k,value in message.items() :
        f.write(f"{k} : {value}\n")

