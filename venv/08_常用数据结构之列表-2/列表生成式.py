# 创建一个取值范围在1到99且能被3或者5整除的数字构成的列表。
items = []
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        items.append(i)
print(items)

items2 = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items2)

# 有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方。
num1 = list(range(1,10))
num2 = []
for i in num1:
    num2.append(i**2)
print(num2)

num3 = list(range(1, 10))
num4 = [i**2 for i in num3]
print(num4)

# 有一个整数列表nums1，创建一个新的列表num5，将nums5中大于50的元素放到num6中。
num5 = [1, 10, 99, 88, 12]
num6 = [i for i in num5 if i > 50]
print(num6)