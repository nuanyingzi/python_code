person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.get('name'))
print(person.get('sex'))
print(person.get('sex', True))

# 如果需要获取字典中所有的键，可以使用keys方法；如果需要获取字典中所有的值，可以使用values方法。字典还有一个名为items的方法，它会将键和值组装成二元组，通过该方法来遍历字典中的元素也是非常方便的。
print(person.keys())
print(person.values())
print(person.items())
for key, value in person.items():
    print(f'{key}: {value}')

# 字典的update方法会用一个字典更新另一个字典中的键值对。例如，有两个字典x和y，当执行x.update(y)操作时，x跟y相同的键对应的值会y中的值被更新，而y中有但x中没有的键值对会直接添加到x中
person1 = {'name': '王大锤', 'age': 25, 'height': 178}
person2 = {'sex': '男', 'addr': '成都市武侯区科华北路62号1栋101'}
person1.update(person2)
print(person1)

# 可以通过pop或popitem方法从字典中删除元素，前者会返回键对应的值，但是如果字典中不存在指定的键，会引发KeyError错误；后者在删除元素时，会返回键和值组成的二元组。字典的clear方法会清空字典中所有的键值对
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.pop('age'))
# print(person.pop('age1'))
print(person)
print(person.popitem())
print(person)
person.clear()
print(person)

# 跟列表一样，从字典中删除元素也可以使用del关键字，在删除元素的时候如果指定的键索引不到对应的值，一样会引发KeyError错误
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
del person['age']
print(person)