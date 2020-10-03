file_name = "D:\\pycharm\\stock.txt"
stockmessage = {}
stockNameinfo = {}
stockNuminfo = {}
with open(file_name,"r",encoding="utf-8") as f :
    while True :
        line = f.readline()
        if len(line) == 0:
            break
        line = line.strip()
        if not line :
            continue
        linelist = line.split("|")
        stockName = linelist[0].strip()
        stockNum = linelist[1].strip()
        stockNameinfo[stockName] = f"{stockName} : {stockNum}"
        stockNuminfo[stockNum] = f"{stockName} : {stockNum}"
while True :
    inputMessage = input("请输入要查询的股票名称或代码: ")
    if inputMessage.isdigit():
        if len(inputMessage) < 6 :
            print("请输入完整的6位股票代码")
        elif inputMessage in stockNuminfo:
            print(stockNuminfo[inputMessage])
        else:
            print("查询不存在")
    else:
        if inputMessage in stockNameinfo :
            print(stockNameinfo[inputMessage])
        else:
            print("查询不存在")


