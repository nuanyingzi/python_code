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

# 性质判断
s91 = 'Hello world'
print(s91.startswith('He'))
print(s91.endswith('ld'))
print(s91.startswith('he'))
s92 = 'abc123456'
print(s92.isalnum()) # 判断字符串是不是由字母和数字构成的
print(s92.isdigit()) # 用来判断字符串是不是完全由数字构成的
print(s92.isalpha()) # 判断字符串是不是完全由字母构成的

# 格式化字符串
s101 = 'hello,world'
print(s101.center(20, '*'))
print(s101.rjust(20))
print(s101.ljust(20, '~'))
print('33'.zfill(5)) # 字符串的左侧补零
print('-33'.zfill(5))

# 修剪操作
# strip()将原字符串修剪掉左右两端指定字符之后的字符串，默认是修剪空格字符
s111 = '   jackfrued@126.com  '
print(s111.strip())
s112 = '~你好世界~'
print(s112.lstrip('~'))
print(s112.rstrip('~'))

# 替换操作
# replace() 第一个参数是被替换的内容，第二个参数是替换后的内容，还可以通过第三个参数指定替换的次数
s121 = 'hello,world'
print(s121.replace(',', ' '))
print(s121.replace('l', 'p', 1))

# 拆分与合并
# split方法将一个字符串拆分为多个字符串（放在一个列表中），也可以使用字符串的join方法将列表中的多个字符串连接成一个字符串
s131 = 'hello,world'
words = s131.split(',')
print(words)
print('~'.join(words))
s132 = 'I#love#you#so#much'
words2 = s132.split('#')
print(words2)
words3 = s132.split('#', 2)
print(words3)

# 编码和解码
s141 = '赣州'
s142 = s141.encode('utf-8')
print(s142)
s143 = s141.encode('gbk')
print(s143)
print(s142.decode('utf-8'))
print(s143.decode('gbk'))