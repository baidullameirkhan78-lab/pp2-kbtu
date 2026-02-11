# 1) ең қарапайым класс
class Person:
    pass  # әзірге ештеңе жоқ

p = Person()
print(type(p))


# 2) класс ішінде айнымалы
class Dog:
    animal = "Dog"

d = Dog()
print(d.animal)


# 3) класс ішінде метод
class Cat:
    def speak(self):
        print("Meow")

c = Cat()
c.speak()


# 4) айнымалы + метод
class Car:
    brand = "BMW"

    def show_brand(self):
        print(self.brand)

car = Car()
car.show_brand()


# 5) бірнеше объект
class Student:
    def say_hi(self):
        print("Hi!")

s1 = Student()
s2 = Student()

s1.say_hi()
s2.say_hi()
