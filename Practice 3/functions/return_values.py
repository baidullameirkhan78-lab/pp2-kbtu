# 1) санды қайтарады
def get_number():
    return 5  # 5 санын қайтарады

print(get_number())


# 2) екі санның қосындысы
def add(a, b):
    return a + b  # қосындысын қайтарады

print(add(3, 5))


# 3) мәтін қайтарады
def say_hello(name):
    return "Hello, " + name  # амандасу мәтінін қайтарады

print(say_hello("Ali"))


# 4) квадрат
def square(x):
    return x * x  # квадратын қайтарады

result = square(4)
print(result)


# 5) True немесе False қайтарады
def is_even(n):
    return n % 2 == 0  # жұп болса True

print(is_even(6))
