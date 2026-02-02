# 1. Skip 2
for i in range(5):
    if i == 2:
        continue
    print(i)


# 2. Skip even
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i)


# 3. Continue string
for ch in "python":
    if ch == "o":
        continue
    print(ch)


# 4. Skip value
for x in [1, 2, 3, 4]:
    if x == 3:
        continue
    print(x)


# 5. Continue example
for i in range(6):
    if i < 3:
        continue
    print(i)
