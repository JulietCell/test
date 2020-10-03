def convert4digits(dight):
    list = ['零','壹','贰','叄','肆','伍','陆','柒','捌','玖']
    if len(dight) <= 1:
        convert = list[int(dight)]
        print(convert)
    elif len(dight) <=2 :
        convert = list[int(dight[0])]+"拾"+list[int(dight[1])]
        convert = convert.replace("零拾","").replace("壹拾","拾").replace("拾零","拾")
        print(convert)
    elif len(dight) <= 3:
        convert = list[int(dight[0])]+"佰"+list[int(dight[1])]+"拾"+list[int(dight[2])]
        convert = convert.replace("零佰","").replace("零拾","零").replace("拾零","拾").replace("零零","").replace("零","")
        print(convert)
    elif len(dight) <= 4:
        convert = list[int(dight[0])]+"仟"+list[int(dight[1])]+"佰"+list[int(dight[2])]+"拾"+list[int(dight[3])]
        convert = convert.replace("零仟","").replace("零佰","零").replace("零拾","").replace("拾零","").replace("零零","").replace("零","")
        print(convert)
    else:
        print("请输入四位以内的数字")

convert4digits('14')
convert4digits('40')
convert4digits('340')
convert4digits('1004')
convert4digits('1234')
convert4digits('10040')

convert4digits('20')
convert4digits('300')
convert4digits('4000')

convert4digits("01")
convert4digits("025")
convert4digits("007")
convert4digits("0026")
convert4digits("0009")