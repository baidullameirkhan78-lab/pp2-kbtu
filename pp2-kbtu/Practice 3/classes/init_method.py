# 1) негізгі мысал
class Student:
    def __init__(self, name):
        self.name = name  # объектке ат береміз

s = Student("Ali")
print(s.name)


# 2) бірнеше параметр
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c = Car("BMW", 2020)
print(c.brand, c.year)


# 3) есептеу
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(circle.area())


# 4) default мән
class Person:
    def __init__(self, name="Guest"):
        self.name = name

p = Person()
print(p.name)


# 5) объект туралы ақпарат
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

b = Book("Python", "Ali")
print(b.title, "-", b.author)
