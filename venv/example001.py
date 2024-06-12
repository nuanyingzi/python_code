import math

# f = float(input("请输入华氏温度："))
# c = (f - 32) / 1.8
# print('%.1f华氏度等于%.1f摄氏度' % (f, c))

radius = float(input("请输入⚪的半径："))
c = 2 * math.pi * radius
s = math.pi * radius ** 2
print('周长：%.2f' % c)
print('面积：%.2f' % s)