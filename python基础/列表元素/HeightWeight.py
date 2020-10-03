#计算x个学生的身高，体重，并计算平均值
x=3
def askinfo() :
    message = []
    for i in range(1,x+1):
        ask_height = input("请输入学员"+str(i)+"的身高:")
        message.append(ask_height)
        ask_weight = input("请输入学员"+str(i)+"的体重:")
        message.append(ask_weight)
    return message
message = askinfo()
# print(message)
average_height = str((int(message[0])+int(message[2])+int(message[4]))/3)
average_weight = str((int(message[1])+int(message[3])+int(message[5]))/3)
print("平均身高是"+average_height+"cm")
print("平均体重是"+average_weight+"kg")