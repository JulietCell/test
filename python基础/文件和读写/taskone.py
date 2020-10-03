print("一个小功能，输入数字3，进入程序，修改链接中的P值，使P值+3，如此+3循环，输入任何其他值退出程序")
stat = True
file_path = "prac_filerw.txt"
while stat :
    input_message = input("请输出信息：")
    if input_message == "3":
        with open(file_path,"r",encoding="utf-8") as f :
            lines = f.read().splitlines()
            file_data =""
            for line in lines:
                if not line :
                    file_data +=line +"\n"
                    continue
                if  not "p=" in line :
                    file_data += line +"\n"
                    continue
                old_pline = line.split("p=")[1]
                # print(data0)
                stat2 =True
                i = 0
                while stat2:
                    if old_pline[i].isdigit() :
                        i+=1
                    else:
                        stat2 = False
                p = old_pline[0:i]
                new_p = int(p)+3
                new_pline = old_pline.replace(p,str(new_p))
                # print(new_pline)
                line = line.replace(old_pline,new_pline)
                file_data += line +"\n"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(file_data)
    else:
        stat = False