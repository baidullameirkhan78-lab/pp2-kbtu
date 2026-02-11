# 1) екі ата-анадан метод алу
class Father:
    def work(self):
        print("Father works")

class Mother:
    def cook(self):
        print("Mother cooks")

class Child(Father, Mother):
    pass

c = Child()
c.work()
c.cook()


# 2) бірдей ат болса – бірінші ата-ана
class A:
    def hello(self):
        print("Hello from A")

class B:
    def hello(self):
        print("Hello from B")

class C(A, B):
    pass

obj = C()
obj.hello()  # A


# 3) өз методын қосу
class A:
    def a(self):
        print("A")

class B:
    def b(self):
        print("B")

class D(A, B):
    def d(self):
        print("D")

x = D()
x.a()
x.b()
x.d()


# 4) isinstance
class A:
    pass

class B:
    pass

class C(A, B):
    pass

c = C()
print(isinstance(c, A))
print(isinstance(c, B))


# 5) класс арқылы көру
class A:
    pass

class B:
    pass

class C(A, B):
    pass

print(C.__mro__)  # қай ретпен іздейді
