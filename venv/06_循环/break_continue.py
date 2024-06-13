total = 0
i = 1
while True:
    total += i
    i += 1
    if i > 100:
        break
print(total)

total2 = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    total2 += i
print(total2)

for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{i}x{j}={i*j}', end='\t')
    print()
