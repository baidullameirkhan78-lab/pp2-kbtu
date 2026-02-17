# generators.py

# 1) iter() and next()
def demo_iter_next():
    numbers = [10, 20, 30]
    iterator = iter(numbers)

    print(next(iterator))
    print(next(iterator))
    print(next(iterator))


# 2) Custom Iterator
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


def demo_custom_iterator():
    for num in CountDown(5):
        print(num)


# 3) Generator function using yield
def square_generator(n):
    for i in range(1, n + 1):
        yield i * i


def demo_generator_function():
    for value in square_generator(5):
        print(value)


# 4) Generator expression
def demo_generator_expression():
    gen = (x * 2 for x in range(5))
    for item in gen:
        print(item)


if __name__ == "__main__":
    demo_iter_next()
    demo_custom_iterator()
    demo_generator_function()
    demo_generator_expression()
