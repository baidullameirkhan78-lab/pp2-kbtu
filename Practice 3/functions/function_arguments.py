def greet(name):
    print("Hello,", name)  # берілген атты шығарады

greet("Ali")


def add(a, b):
    print(a + b)  # екі санды қосады

add(3, 5)


def country(name):
    print("I am from", name)  # ел атын шығарады

country("Kazakhstan")


def greet(name="Guest"):
    print("Hello,", name)  # егер аргумент берілмесе Guest болады

greet()


def square(x):
    return x * x  # квадратын қайтарады

print(square(4))
