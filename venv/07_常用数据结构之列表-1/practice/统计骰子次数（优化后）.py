# 优化后
import random

counters = [0] * 6
for _ in range(6000):
    point = random.randrange(1, 7)
    counters[point-1] += 1
for i in range(1, 7):
    print(f'{i}点次数：{counters[i-1]}')