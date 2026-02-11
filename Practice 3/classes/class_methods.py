# 1) класс методтың негізі
class Student:
    school = "KBTU"

    @classmethod
    def get_school(cls):
        return cls.school  # class variable қолданады

print(Student.get_school())


# 2) class variable өзгерту
class Car:
    wheels = 4

    @classmethod
    def change_wheels(cls, number):
        cls.wheels = number  # ортақ мән өзгереді

Car.change_wheels(6)
print(Car.wheels)


# 3) объект арқылы шақыру
class Person:
    species = "Human"

    @classmethod
    def get_species(cls):
        return cls.species

p = Person()
print(p.get_species())


# 4) жаңа объект жасау (factory)
class Book:
    def __init__(self, title):
        self.title = title

    @classmethod
    def create_default(cls):
        return cls("Unknown")  # объект қайтарады

b = Book.create_default()
print(b.title)


# 5) есептеу
class Math:
    pi = 3.14

    @classmethod
    def circle_area(cls, r):
        return cls.pi * r * r

print(Math.circle_area(3))
