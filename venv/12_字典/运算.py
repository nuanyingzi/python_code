person = {'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60, 'addr': '成都市武侯区科华北路62号1栋101'}
# 成员运算
print('name' in person)
print('name1' in person)
# 索引运算
print(person['name'])
print(person['addr'])
person['age'] = 18
person['height'] = 180
person['weight'] = 75
person['tel'] = '18179707913'
person['signature'] = '你的男朋友是一个盖世垃圾，他会踏着五彩祥云去迎娶你的闺蜜'
print(person)

# 循环遍历
for key in person:
    print(f'{key}/t{person[key]}')

