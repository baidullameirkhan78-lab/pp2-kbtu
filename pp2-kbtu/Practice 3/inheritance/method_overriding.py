# 1) негізгі override
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof")  # өзгертілді

d = Dog()
d.speak()


# 2) басқа мысал
class Person:
    def work(self):
        print("Working")

class Programmer(Person):
    def work(self):
        print("Coding")  # override

p = Programmer()
p.work()


# 3) ата-ананың орнына бала метод шақырылады
class Bird:
    def move(self):
        print("Walking")

class FlyingBird(Bird):
    def move(self):
        print("Flying")

b = FlyingBird()
b.move()


# 4) айнымалы бар кезде
class Car:
    def info(self):
        print("This is a car")

class BMW(Car):
    def info(self):
        print("This is BMW")  # override

c = BMW()
c.info()


# 5) parent тип ретінде
class Animal:
    def speak(self):
        print("Animal sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

a = Cat()
a.speak()
