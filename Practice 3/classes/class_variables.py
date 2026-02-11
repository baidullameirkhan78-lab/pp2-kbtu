# 1) ортақ айнымалы
class Student:
    school = "KBTU"  # class variable

s1 = Student()
s2 = Student()

print(s1.school)
print(s2.school)


# 2) өзгерсе – бәріне өзгереді
class Car:
    wheels = 4  # ортақ

c1 = Car()
c2 = Car()

Car.wheels = 6

print(c1.wheels)
print(c2.wheels)


# 3) instance ішінде қолдану
class Person:
    species = "Human"  # class variable

p = Person()
print(p.species)


# 4) instance variable мен class variable айырмашылығы
class Dog:
    animal = "Dog"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

d1 = Dog("Rex")
d2 = Dog("Bob")

print(d1.animal, d1.name)
print(d2.animal, d2.name)


# 5) class арқылы шығару
class Phone:
    brand = "Apple"  # class variable

print(Phone.brand)
