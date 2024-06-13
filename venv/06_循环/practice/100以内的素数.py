# 100以内的素数
# 素数指的是只能被1和自身整除的正整数（不包括1）

for i in range(1, 101):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)