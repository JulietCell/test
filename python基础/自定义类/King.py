from random import randint
import time,sys

# 玩家
class Player:

    def __init__(self,stoneNumber):
        self.stoneNumber = stoneNumber # 灵石数量
        self.warriors = {}  # 拥有的战士，包括弓箭兵和斧头兵

# 战士
class Warrior:

    # 初始化参数是生命值
    def __init__(self, strength):
        self.strength = strength

    # 用灵石疗伤
    def healing(self, stoneCount):
        # 如果已经到达最大生命值，灵石不起作用，浪费了
        if self.strength == self.maxStrength:
            return

        self.strength += stoneCount

        # 不能超过最大生命值
        if self.strength > self.maxStrength:
            self.strength = self.maxStrength


# 弓箭兵 是 战士的子类
class Archer(Warrior):
    # 种类名称
    typeName = '弓箭兵'

    # 雇佣价 100灵石，属于静态属性
    price = 100

    # 最大生命值 ，属于静态属性
    maxStrength = 100


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 20
        elif monster.typeName== '狼妖':
            self.strength -= 80
        else:
            print('未知类型的妖怪！！！')



# 斧头兵 是 战士的子类
class Axeman(Warrior):
    # 种类名称
    typeName = '斧头兵'

    # 雇佣价 120灵石
    price = 120

    # 最大生命值
    maxStrength = 120


    # 初始化参数是生命值, 名字
    def __init__(self, name, strength = maxStrength):
        Warrior.__init__(self, strength)
        self.name = name

    # 和妖怪战斗
    def fightWithMonster(self,monster):
        if monster.typeName== '鹰妖':
            self.strength -= 80
        elif monster.typeName== '狼妖':
            self.strength -= 20
        else:
            print('未知类型的妖怪！！！')

# 鹰妖
class Eagle():
    typeName = '鹰妖'

# 狼妖
class Wolf():
    typeName = '狼妖'

# 森林
class Forest():
    def __init__(self,monster):
        # 该森林里面的妖怪
        self.monster = monster

print('''
***************************************
****           游戏开始             ****
***************************************

'''
)

# 森林数量
forest_num = 7

# 森林 列表
forestList = []

# 为每座森林随机产生 鹰妖或者 狼妖
notification = '前方森林里的妖怪是：'  # 显示在屏幕上的内容
for i in range(forest_num):
    typeName = randint(0,1)
    if typeName == 0:
        forestList.append( Forest(Eagle()) )
    else:
        forestList.append( Forest(Wolf()) )

    notification += \
        f'第{i+1}座森林里面是 {forestList[i].monster.typeName}  '

# 显示 妖怪信息
print(notification,end='')
print("\n\n\n")
#玩家初始的宝石数目
stoneNumber = 1000
play1 = Player(stoneNumber)
#雇佣多少个弓箭兵
while True :
    ArcherNum = int(input("你需要雇佣多少个弓箭兵："))
    if play1.stoneNumber < ArcherNum * Archer.price :
        print("对不起，宝石不够，请减少雇佣数")
    else:
        residualStoneNumber = play1.stoneNumber - ArcherNum * Archer.price
        break
print(f"还剩{residualStoneNumber}个宝石")

#雇佣多少个斧头兵
while True :
    AxemanNum = int(input("你需要雇佣多少个斧头兵："))
    if residualStoneNumber < AxemanNum * Axeman.price:
        print("对不起，宝石不够，请减少雇佣数")
    else:
        residualStoneNumber -= AxemanNum * Axeman.price
        break
print(f"还剩{residualStoneNumber}个宝石")

ArcherList = []
AxemanList = []
ArcherNameList =[]
AxemanNameList = []
#创建弓箭兵实例
for i in range(ArcherNum) :
    ArcherName = input(f"请输入第{i+1}个弓箭兵的名字：")
    ArcherList.append(Archer(ArcherName))
    ArcherNameList.append(Archer(ArcherName).name)

#创建斧头兵实例
for i in range(AxemanNum) :
    AxemanName = input(f"请输入第{i+1}个斧头兵的名字：")
    AxemanList.append(Axeman(AxemanName))
    AxemanNameList.append(Axeman(AxemanName).name)

#玩家的战士初始化
play1.warriors[Archer.typeName] = ArcherList
play1.warriors[Axeman.typeName] = AxemanList

#循环7次，在每个森林打怪
for i in range(7) :
    if not (ArcherList or AxemanList):
        print("游戏结束，未通关")
        print(f"剩余宝石{residualStoneNumber}")
        break
    print(f"目前已经进入第{i+1}个森林")
    while True :
        selectType = input("请输入出站战士的类型，弓箭兵或者斧头兵：")
        if selectType == "弓箭兵" :
            if ArcherList :
                print("可选择的弓箭兵如下：")
                for Archer in play1.warriors[selectType] :
                    print(Archer.name)
                selectName = input("请选择如上其中一位需要出战的弓箭兵：")
                k = ArcherNameList.index(selectName)
                ArcherList[k].fightWithMonster(forestList[i].monster)
                if ArcherList[k].strength > 0 :
                    print("击败怪物成功")
                    print(f"剩余宝石数为{residualStoneNumber}")
                    xuemessage = input("是否用灵石给战士补养，消耗1个灵石可以为生命值加1：")
                    if xuemessage == "是":
                        xueNum = int(input("请输入补血值："))
                        AxemanList[k].healing(xueNum)
                        residualStoneNumber -= xueNum
                        print("补养成功")
                    break
                else:
                    print(f"{ArcherList[k].name}阵亡，请选择其他战士")
                    ArcherList.pop(k)
                    if (ArcherList or AxemanList) :
                        continue
                    if not (ArcherList or AxemanList):
                        break
            # else:
            #     print("没有可以使用的弓箭兵，请选择其他种类的战士")

        elif selectType == "斧头兵":
            if AxemanList :
                print("可选择的斧头兵如下：")
                for Axeman in play1.warriors[selectType] :
                    print(Axeman.name)
                selectName = input("请选择如上其中一位需要出战的斧头兵兵：")
                k = AxemanNameList.index(selectName)
                AxemanList[k].fightWithMonster(forestList[i].monster)
                if AxemanList[k].strength > 0 :
                    print("击败怪物成功")
                    print(f"剩余宝石数为{residualStoneNumber}")
                    xuemessage = input("是否用灵石给战士补养，消耗1个灵石可以为生命值加1：")
                    if xuemessage == "是":
                        xueNum = int(input("请输入补血值："))
                        AxemanList[k].healing(xueNum)
                        residualStoneNumber -= xueNum
                        print("补养成功")
                    break
                else:
                    print(f"{AxemanList[k].name}阵亡，请选择其他战士")
                    AxemanList.pop(k)
                    if (ArcherList or AxemanList):
                        continue
                    if not (ArcherList or AxemanList):
                        break
            # else:
            #     print("没有可以使用的斧头兵，请选择其他种类的战士")
if (ArcherList or AxemanList) :
    print("游戏通关")
    print(f"剩余宝石{residualStoneNumber}个")






