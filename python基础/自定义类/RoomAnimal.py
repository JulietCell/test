class Tiger():
    name = "老虎"
    def __init__(self,weight=200):
        self.weight = weight

    def call(self):
        print("Wow!!")
        self.weight -= 5

    def feed(self,food):
        if food == "肉" :
            self.weight +=10
            print("喂食正确，体重+10")
        else:
            self.weight -= 10
            print("喂食错误，体重-10")

class Sheep():
    name = "羊"

    def __init__(self, weight=100):
        self.weight = weight

    def call(self):
        print("mie~~")
        self.weight -= 5

    def feed(self, food):
        if food == "草":
            self.weight += 10
            print("喂食正确，体重+10")
        else:
            self.weight -= 10
            print("喂食错误，体重-10")

class Room():
    def __init__(self,number,animal):
        self.number = number
        self.animal = animal

from random import randint
rooms = []
#生成10个Room实列,10个房间存入数组rooms
for i in range(1,11) :
    if randint(0,1) == 1 :
        animal =Tiger()
    else:
        animal = Sheep()
    room = Room(i,animal)
    rooms.append(room)
i =0
while i <5 :
    roomNumber = randint(1,10)
    roomObj = rooms[roomNumber-1]
    print(f"当前的房间号为{roomObj.number},房间中的动物为{roomObj.animal.name}")
    inputmessage = input("请选择喂食或者敲门：")
    if inputmessage == "喂食":
        food = input("选择喂食肉或者草？")
        roomObj.animal.feed(food.strip())
    else:
        roomObj.animal.call()
    print(f"当前房间的动物{roomObj.animal.name}的体重为{roomObj.animal.weight}")
    i +=1
print("\n\n")
for room in rooms :
    print(f"房间编号为{room.number}的动物{room.animal.name}目前的体重为{room.animal.weight}")


