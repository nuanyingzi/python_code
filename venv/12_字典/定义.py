
xinhua = {
    '麓': '山脚下',
    '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名',
    '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}

print(xinhua)

person  = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': '成都市武侯区科华北路62号1栋101',
    'tel': '13122334455',
    'emergence contact': '13800998877'
}
print(person)

# dict函数(构造器)中的每一组参数就是字典中的一组键值对
person = dict(name='王大锤', age=55, height=168)
print(person)

# 可以通过Python内置函数zip压缩两个序列并创建字典
item1 = dict(zip('ABCDEFG', '1234567'))
print(item1)
item2 = dict(zip('ABCDEF', range(1,6)))
print(item2)

# 用字典生成式语法创建字典
item3 = {x: x**3 for x in range(1,6)}
print(item3)

person = {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}
print(len(person))
for key in person:
    print(key)