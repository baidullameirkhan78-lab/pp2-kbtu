# 1. Skip 3
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)


# 2. Skip even numbers
i = 0
while i < 6:
    i += 1
    if i % 2 == 0:
        continue
    print(i)


# 3. Skip zero
x = -2
while x <= 2:
    x += 1
    if x == 0:
        continue
    print(x)


# 4. Continue example
i = 1
while i <= 5:
    if i == 4:
        i += 1
        continue
    print(i)
    i += 1


# 5. Skip specific value
n = 0
while n < 4:
    n += 1
    if n == 2:
        continue
    print("n =", n)
