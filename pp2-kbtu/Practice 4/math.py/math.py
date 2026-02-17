# math.py

import math
import random


def demo_builtin_math():
    numbers = [3, -7, 10, 2]

    print("Min:", min(numbers))
    print("Max:", max(numbers))
    print("Absolute:", abs(-5))
    print("Round:", round(3.14159, 2))
    print("Power:", pow(2, 3))


def demo_math_module():
    print("Square root:", math.sqrt(16))
    print("Ceil:", math.ceil(3.2))
    print("Floor:", math.floor(3.8))
    print("Sin(pi/2):", math.sin(math.pi / 2))
    print("Pi:", math.pi)
    print("E:", math.e)


def demo_random_module():
    print("Random float:", random.random())
    print("Random int:", random.randint(1, 10))

    items = ["apple", "banana", "cherry"]
    print("Random choice:", random.choice(items))

    random.shuffle(items)
    print("Shuffled list:", items)


if __name__ == "__main__":
    demo_builtin_math()
    demo_math_module()
    demo_random_module()
