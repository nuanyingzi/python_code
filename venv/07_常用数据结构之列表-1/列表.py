items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ['Python', 'Java', 'JavaScript']
print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
items5 += items6
print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]

print(items6 * 3)  # [45, 58, 29, 45, 58, 29, 45, 58, 29]
print(items7 * 2)  # ['Python', 'Java', 'JavaScript', 'Python', 'Java', 'JavaScript']

print(29 in items6)
print(11 in items6)
print('Php' not in items7)
print('Python' not in items7)

items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[0])   # apple
print(items8[2])   # pitaya
print(items8[4])   # watermelon
items8[2] = 'durian'
print(items8)      # ['apple', 'waxberry', 'durian', 'peach', 'watermelon']
print(items8[-5])  # 'apple'
print(items8[-4])  # 'waxberry'
print(items8[-1])  # watermelon
items8[-4] = 'strawberry'
print(items8)      # ['apple', 'strawberry', 'durian', 'peach', 'watermelon']

print(items8[1:3:1]) # ['strawberry', 'durian']
print(items8[0:5:2]) # ['apple', 'durian', 'watermelon']
print(items8[-4:-2:1])   # ['strawberry', 'durian']
print(items8[-2:-6:-1])  # ['peach', 'durian', 'strawberry', 'apple']

print(items8[:3]) # ['apple', 'strawberry', 'durian']
print(items8[::2]) # ['apple', 'durian', 'watermelon']

items8[1:3] = ['x', 'o']
print(items8) # ['apple', 'x', 'o', 'peach', 'watermelon']

nums1 = [1,2,3,4]
nums2 = list(range(1,5))
nums3 = [3,2,1]

print(nums1 == nums2)
print(nums1 != nums2)
print(nums1 <= nums3)
print(nums2 >= nums3)

languages = ['Php', 'Python', 'Java', 'Go']
for index in range(len(languages)):
    print(languages[index])

for language in languages:
    print(language)