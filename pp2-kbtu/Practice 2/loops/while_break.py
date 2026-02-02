# 1. break with number
i = 1
while True:
    print(i)
    if i == 3:
        break
    i += 1


# 2. Stop at 5
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1


# 3. Password check
while True:
    password = "1234"
    if password == "1234":
        print("Access")
        break


# 4. Infinite loop stop
i = 0
while True:
    print("Hello")
    i += 1
    if i == 2:
        break


# 5. Break with condition
n = 1
while n <= 10:
    if n > 6:
        break
    print(n)
    n += 1
