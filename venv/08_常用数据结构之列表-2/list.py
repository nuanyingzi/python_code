languages = ['Python', 'Java', 'Php', 'Go']
languages.append('JavaScript')

if 'Java' in languages:
    languages.remove('Java')
print(languages)
languages.pop()
print(languages)
temp = languages.pop(1)
print(temp)
languages.append(temp)
print(languages)
languages.clear()
print(languages)

languages2 = ['Python', 'Java', 'Php', 'Go', 'Python']
languages2.remove('Python')
print(languages2)

items2 = ['Python', 'Java', 'Php', 'Go', 'Python']
del items2[1]
print(items2)

items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.index('Python'))
# 从索引位置1开始查找'Python'
print(items.index('Python', 1))
print(items.count('Python'))
# 从索引位置3开始查找'Java'
# print(items.index('Java', 3))

items3 = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
items3.sort()
print(items3)
items3.reverse()
print(items3)
