import time

# 从1到100的整数求和
total = 0
for i in range(1, 101):
    total += i
print(total)

# 从1到100的偶数求和
total2 = 0
for i in range(2, 101, 2):
    total2 += i
print(total2)

total3 = sum(range(2, 101, 2))
print(total3)