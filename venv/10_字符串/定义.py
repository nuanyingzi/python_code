s1 = 'Hello world'
s2 = "你好，世界❤️"
s3 = '''hello,
wonderful
world!'''
print(s1)
print(s2)
print(s3)

# 转义字符
s11 = '\'hello world\''
s12 = '\\hello world\\'
print(s11)
print(s12)

# 原始字符串
# s13 = '\it \is \time \to \read \now'
s14 = r'\it \is \time \to \read \now'
# print(s13)
print(s14)

# 字符串的运算
s21 = 'hello' + ',' + 'world'
print(s21)
s22 = '!' * 3
print(s22)
s21 += s22
print(s21)
s21 *= 2
print(s21)

# 成员运算
s31 = 'hello, world'
s32 = 'goodbye, world'
print('wo' in s31)
print('wo' not in s32)
print(s31 in s32)

# 获取字符串长度
s41 = 'hello world'
s42 = 'goodbye, world'
print(len(s41))
print(len(s42))

# 索引和切片
s51 = 'abc123456'
n = len(s51)
print(n)
print(s51[0], s51[-n])
print(s51[n-1], s51[-1])
print(s51[:])
print(s51[::-1])

# 字符的遍历
s61 = 'hello'
for s in s61:
    print(s)

# 字符串的方法
s71 = 'hello,world!'
print(s71.capitalize()) # 字符串首字母大写
print(s71.title()) # 字符串每个单词首字母大写
print(s71.upper()) # 字符串变大写
print(s71.lower()) # 字符串变小写

# 查找操作
s81 = 'Hello,world!'
print(s81.find('or'))
print(s81.find('or', 8))
print(s81.index('lo'))
print(s81.rindex('o')) # 逆向查找
