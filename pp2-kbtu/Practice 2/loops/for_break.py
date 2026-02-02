# 1. Break at 3
for i in range(5):
    if i == 3:
        break
    print(i)


# 2. Stop loop
for x in range(1, 10):
    if x == 6:
        break
    print(x)


# 3. Break with string
for ch in "hello":
    if ch == "l":
        break
    print(ch)


# 4. Find number
for i in range(10):
    if i == 7:
        print("Found")
        break


# 5. Break example
for n in [1, 2, 3, 4]:
    if n == 3:
        break
    print(n)
