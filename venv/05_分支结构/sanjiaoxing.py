# 输入三条边的长度，如果能构成三角形就计算周长和面积；否则给出“不能构成三角形”的提示。
import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and b + c > a and c + a > b:
    perimeter = a + b + c
    print(f'周长：{perimeter}')
    perimeter2 = perimeter / 2
    # 海伦公式：已知三角形三边长分别为a、b、c, 则它的面积为：S = √(p(p−a)(p−b)(p−c)) 其中p为半周长：即：p = (a + b + c) /2
    # 这公式为海伦（Heron）公式
    area = math.sqrt(perimeter2 * (perimeter2 - a) * (perimeter2 - b) * (perimeter2 - c))
    print(f'面积：{area}')
else:
    print('不能构成三角形')