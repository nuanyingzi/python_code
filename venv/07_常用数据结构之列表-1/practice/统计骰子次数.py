# 将一颗色子掷6000次，统计每种点数出现的次数。这个任务对大家来说应该是非常简单的，我们可以用1到6均匀分布的随机数来模拟掷色子，然后用6个变量分别记录每个点数出现的次数
import random

f1 = f2 = f3 = f4 = f5 = f6 = 0
times = 0
while times <= 6000:
    point = random.randrange(1, 7)
    match point:
        case 1:
            f1 += 1
        case 2:
            f2 += 1
        case 3:
            f3 += 1
        case 3:
            f3 += 1
        case 4:
            f4 += 1
        case 5:
            f5 += 1
        case 6:
            f6 += 1

    times += 1
print(f'点数1次数:{f1}, 点数2次数:{f2}, 点数3次数:{f3}, 点数4次数:{f4}, 点数5次数:{f5},点数6次数:{f6}')




