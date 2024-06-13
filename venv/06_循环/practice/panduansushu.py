# 判断素数
# 要求：输入一个大于1的正整数，判断它是不是素数。
# 素数指的是只能被1和自身整除的大于1的整数。例如对于正整数n，我们可以通过在2到n-1之间寻找有没有n的因子，来判断它到底是不是一个素数

desc = "是素数"
number = int(input("请输入一个正整数："))
for i in range(2, number):
    if number % i == 0:
        desc = "不是素数"
        break
print(desc)