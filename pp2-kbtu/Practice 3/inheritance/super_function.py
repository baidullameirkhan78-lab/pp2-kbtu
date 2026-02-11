# 1) parent методты шақыру
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()  # ата-ананы шақырдық
        print("Woof")

d = Dog()
d.speak()


# 2) __init__ ішінде
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)  # parent init
        self.grade = grade

s = Student("Ali", 5)
print(s.name, s.grade)


# 3) қосымша әрекет
class Car:
    def info(self):
        print("Car info")

class BMW(Car):
    def info(self):
        super().info()
        print("BMW info")

c = BMW()
c.info()


# 4) parent + child бірге
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        super().hello()
        print("Hello from B")

b = B()
b.hello()


# 5) super болмаса айырмашылығы
class A:
    def show(self):
        print("A")

class C(A):
    def show(self):
        print("C only")  # parent шақырылмайды

obj = C()
obj.show()
