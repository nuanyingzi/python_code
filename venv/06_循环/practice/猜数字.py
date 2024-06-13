# 猜数字
# 计算机出一个1到100之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息“大一点”、“小一点”或“猜对了”，如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
import random

number = random.randrange(1, 101)
counter = 1
while True:
    x = int(input("请输入您猜的数字："))
    counter += 1
    if x > number:
        print("小一点")
    elif x < number:
        print("大一点")
    else:
        print("猜对了")
        break
print("次数：", counter)