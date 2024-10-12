from math import factorial as f

# 输入m n，计算组合C(m, n)的值
m = int(input('m = '))
n = int(input('n = '))
# 计算m的阶乘
fm = 1
for i in range(1, m+1):
    fm *= i
# 计算n的阶乘
fn = 1
for i in range(1, n+1):
    fn *= i
# 结算m-n的阶乘
fk = 1
for i in range(1, m-n+1):
    fk *= i
# 计算C(m,n)
print(fm // fn // fk)



# 声明一个求阶乘的函数
def fac(num):
    result = 1
    for number in range(1, num+1):
        result *= number
    return result
m = int(input('m = '))
n = int(input('n = '))
print(fac(m) // fac(n) // fac(m-n))

# 用自带函数求
m = int(input('m = '))
n = int(input('n = '))
print(f(m) // f(n) // f(m-n))