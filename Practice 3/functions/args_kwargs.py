# 1) *args – кез келген сандар
def add_all(*args):
    print(sum(args))  # барлық аргументтерді қосады

add_all(1, 2, 3)


# 2) *args – элементтерді шығару
def show_numbers(*args):
    for num in args:
        print(num)  # әр санды жеке шығарады

show_numbers(5, 10, 15)


# 3) **kwargs – dictionary
def show_info(**kwargs):
    print(kwargs)  # барлық мәліметті шығарады

show_info(name="Ali", age=18)


# 4) **kwargs – кілт пен мән
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)  # key және value

print_info(name="Ali", country="Kazakhstan")


# 5) бірге қолдану
def example(a, *args, **kwargs):
    print(a)       # бірінші міндетті аргумент
    print(args)    # қалғандары
    print(kwargs)  # атпен берілгендер

example(1, 2, 3, name="Ali")
