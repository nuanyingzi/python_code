# CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简化后的规则是：玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；玩家如果摇出其他点数则游戏继续，
# 玩家重新摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；其他点数玩家继续摇骰子，直到分出胜负。为了增加代码的趣味性，我们设定游戏开始时玩家有1000元的赌注，每局游戏开始之前，玩家先下注，如果玩家获胜就可以获得对应下注金额的奖励，如果庄家获胜，
# 玩家就会输掉自己下注的金额。游戏结束的条件是玩家破产（输光所有的赌注）

import random
money = 1000

while money > 0:
    print(f'你当前的余额:{money}')
    wager = int(input('请下注：'))
    while True:
        if 0 < wager <= money:
            break
    prime = random.randrange(1, 7) + random.randrange(1, 7)
    print(f'玩家摇出了{prime}点')
    if prime == 7 or prime == 11:
        money += wager
        print('玩家胜\n')
    elif prime == 2 or prime == 3 or prime == 12:
        money -= wager
        print('庄家胜\n')
    else:
        while True:
            nextPrime = random.randrange(1, 7) + random.randrange(1, 7)
            print(f'玩家摇出了{nextPrime}点')
            if nextPrime == prime:
                print('玩家胜\n')
                money += wager
                break
            elif nextPrime == 7:
                money -= wager
                print('庄家胜\n')
                break
print('你破产了')



