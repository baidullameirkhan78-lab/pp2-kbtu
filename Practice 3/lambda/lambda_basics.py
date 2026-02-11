# 1) екі санды қосу
add = lambda a, b: a + b  # қосынды

print(add(3, 5))


# 2) квадрат
square = lambda x: x * x  # квадрат

print(square(4))


# 3) жұп сан ба?
is_even = lambda n: n % 2 == 0  # True немесе False

print(is_even(6))


# 4) string ұзындығы
length = lambda s: len(s)  # ұзындығын табады

print(length("Python"))


# 5) үлкен санды табу
maximum = lambda a, b: a if a > b else b  # максимум

print(maximum(10, 7))
