# Single Level Inheritance

class Animal():
    def food(self):
        print("Eat biscuits")
        
class Dog(Animal):
    def sound(self):
        print("Dog Barks")

a = Animal()
dog = Dog()
dog.food()
dog.sound()
a.food()

#Multi Level Inheritance

class House():
    def place(self):
     print("It is a place to live")
class kitchen(House):
    def place1(self):
     print("It is a place to cook")
class DiningHall(kitchen):
    def place2(self):
     print("It is a place to have food")
    
d = DiningHall()
d.place()
d.place1()
d.place2()

# Hierarchical Inheritance

class Animal():
    def sound(self):
        print("Animals makes sound")
        
class Dog(Animal):
    def barks(self):
        print("Dogs barks")
        
class Cat(Animal):  
    def meow(self):
        print("Cat Meow")

d = Dog()
c = Cat()

d.barks()
d.sound()
c.meow()
c.sound()      

# Hybrid Inheritance

class A:
    def method_a(self):
        print("Method from A")

class B(A):
    def method_b(self):
        print("Method from B")

class C:
    def method_c(self):
        print("Method from C")

class D(B, C):
    def method_d(self):
        print("Method from D")

d = D()
d.method_a()
d.method_b()
d.method_c()
d.method_d()


        
