# 1) ең қарапайым мұрагерлік
class Animal:
    def speak(self):
        print("Sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()  # ата-анадан келді


# 2) жаңа метод қосу
class Animal:
    def eat(self):
        print("Eating")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.eat()
c.speak()


# 3) override (ата-ананың методын өзгерту)
class Animal:
    def speak(self):
        print("Some sound")

class Bird(Animal):
    def speak(self):
        print("Tweet")  # өзгертілді

b = Bird()
b.speak()


# 4) ата-ананың айнымалысын алу
class Person:
    species = "Human"

class Student(Person):
    pass

s = Student()
print(s.species)


# 5) isinstance тексеру
class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()
print(isinstance(d, Animal))  # True
