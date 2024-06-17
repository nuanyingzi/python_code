import timeit

t1 = (99, 89, 91)
t2 = ('哈哈', 'haha', 90, False)

# 查看变量的类型
print(type(t1))
print(type(t2))

# 查看元组中元素的数量
print(len(t1))
print(len(t2))
#  索引运算
print(t1[0])
print(t2[0])
print(t2[-2])

# 切片运算
print(t1[:2])
print(t2[::3])

# 遍历
for elem in t2:
    print(elem)

# 成员运算
print('haha' in t2)
print(0 in t1)
print('das' not in t2)

# 拼接运算
t3 = t1 + t2
print(t3)

# 比较运算
print(t1 == t3)            # False
print(t1 >= t3)            # False
print(t1 <= (35, 11, 99))  # False

# 一个元组中如果有两个元素，我们就称之为二元组；一个元组中如果五个元素，我们就称之为五元组。需要提醒大家注意的是，()表示空元组，但是如果元组中只有一个元素，需要加上一个逗号，否则(
# )就不是代表元组的字面量语法，而是改变运算优先级的圆括号，所以('hello', )和(100, )才是一元组，而('hello')和(100)只是字符串和整数。我们可以通过下面的代码来加以验证。
a = ()
print(type(a))
b = (1)
print(type(b))
c = (1,)
print(type(c))

# 打包操作
aa = 1, 12, 100
print(type(aa))
print(aa)

# 解包操作
i, j, k = aa
print(i, j, k)

# 有一种解决变量个数少于元素的个数方法，就是使用星号表达式。通过星号表达式，我们可以让一个变量接收多个值，代码如下所示。需要注意两点：首先，用星号表达式修饰的变量会变成一个列表，列表中有0个或多个元素；其次，在解包语法中，星号表达式只能出现一次。
i, *j = aa
print(i, j)

a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'Hello'
print(a, b, c)

print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))

infos = ('赣州', 'haha', 18, 180)
# 将元组转换成列表
print(list(infos))

frts = [1, 210, 190]
# 将列表转换成元组
print(tuple(frts))

