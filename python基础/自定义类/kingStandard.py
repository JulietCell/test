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
print(notification,end='',flush=True)

# 10秒后删除屏幕信息
time.sleep(1)
print('\b'*300)

#创建玩家
player = Player(1000)
print(f"你现在有{player.stoneNumber}灵石")

#雇佣战士的流程
def hireWarriors():
    menu = '''
        请选择雇佣兵种
        1 - 弓箭兵
        2 - 斧头兵
        0 - 雇佣完成，退出
        ：'''
    while True:
        choice = input(menu)
        if choice not in ["1","2","0"]:
            print("输入错误")
            continue
        if choice == "0" :#退出雇佣流程
            return
        if choice == "1" :
            hireclass = Archer
        else:
            hireclass = Axeman
        if hireclass.price > player.stoneNumber :
            print("灵石不足，您只有{player.stoneNumber}灵石")
            continue

        #给战士命名
        while True:
            warriorsName = input("请给他起个名字：")
            if not warriorsName :   #没有输入内容
                continue
            if warriorsName in player.warriors :
                print("这个名字已经被使用")
                continue
            break

        #招入战士
        player.warriors[warriorsName] = hireclass(warriorsName)

        #支付灵石
        # player.stoneNumber -= hireclass(warriorsName).price
        player.stoneNumber -= hireclass.price

        print(f'雇佣成功，您现在剩余灵石{player.stoneNumber}')

#雇佣弓箭兵和斧头兵
hireWarriors()

#打印出麾下的战士情况和灵石数量
def printInfo():
    print("\n您麾下的战士情况如下")
    for name,warrior in player.warriors.items():
        print(f"{name}: {warrior.typeName} 生命值 {warrior.strength}") #.后面没有自动接属性？

    print(f'您的灵石还剩余{player.stoneNumber}')

printInfo()

for name,warrior in player.warriors.items():
    print(f'{warrior.typeName} : {name}')

print("\n\n ****** 出发啦 *******")
# 每个森林关卡
for no, forest in enumerate(forestList):
    # 如果战士队列为空，游戏还没有通关，就失败了
    if not player.warriors:
        print('您麾下没有战士，游戏结束')
        exit()

    print(f'\n\n ### 现在到了第 {no+1} 座森林 ### ')

#派出战士，森林打怪
    while True:
        while True:
            warriorName = input("你要派出的战士是? ")
            if warriorName not in player.warriors :
                print("没有这个战士")
                continue
            break
        warrior = player.warriors[warriorName]
        print(f"当前森林里面是{forest.monster.typeName}")
        warrior.fightWithMonster(forest.monster)
        print(f'经过战斗，你的战士{warriorName}，生命值还有{warrior.strength}')

        #如果生命值小于0，则死去，从队伍里消失
        if warrior.strength <= 0 :
            print("他,阵亡了")
            player.warriors.pop(warriorName)
            continue
        else:
            break

    input('\n\n过关了，按回车键继续...')
    # 过关后，选择给战士疗伤
    while True:
        printInfo()

        op = input('''\n请输入疗伤战士名字和灵石数量，格式如为：姓名+20
直接回车退出疗伤：''')
        if not op :
            break
        if op.count("+") != 1:
            print("输入格式错误")
            continue

        name,stoneCount = op.split("+")
        name = name.strip()
        stoneCount = stoneCount.strip()
        if name not in player.warriors :
            print("姓名错误")

        if not stoneCount.isdigit():
            print("灵石数量必须是数字")
            continue

        stoneCount =int(stoneCount)
        if stoneCount > player.stoneNumber :
            print(f'灵石数量没有{stoneCount}这么多了')
            continue
        player.warriors[name].healing(stoneCount)
        player.stoneNumber -= stoneCount

print(f'\n\n *** 游戏结束，您剩余的灵石为{player.stoneNumber} ****')

