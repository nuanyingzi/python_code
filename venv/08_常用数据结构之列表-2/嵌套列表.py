import random

scores = [
    [95, 83, 92],
    [80, 75, 82],
    [92, 97, 90],
    [80, 78, 69],
    [65, 66, 89]
]
print(scores)
print(scores[0])
print(scores[0][1])

# 产生随机数的方式来生成5个学生3门课程的成绩并保存在列表中，使用列表生成式
scores2 = [[random.randrange(60, 101) for _ in range(3)] for i in range(1, 6)]
print(scores2)