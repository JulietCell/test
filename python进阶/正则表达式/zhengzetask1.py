import re
filename = f"D:\pypath\zhengze\stock.txt"
with open(filename,"r",encoding="utf-8") as f :
    content = f.read()
while True :
    inputmessage = input("请输入股票名称关键字或者代码：")
    inputmessage = inputmessage.strip()
    if not inputmessage :
        continue
    if inputmessage.isdigit():
        if len(inputmessage) <6 :
            print("请输入完整的6位股票代码")
            continue
    keyword = f'^.*{inputmessage}.*$'
    retlist = re.findall(keyword,content,re.M)[:10]
    for one in retlist :
        print(one)