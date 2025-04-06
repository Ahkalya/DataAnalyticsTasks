#OVERLOADING
class overloading:
    def Details(self,name=None,age=None):
        if name and age:
          print(f"name : {name}, age : {age}")
        elif name:
           print(f"name : {name}")
        else:
            print("No details provided")

s = overloading()
s.Details("Alice",25)
s.Details("Bob")
s.Details()

#OVERRIDING

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("The dog barks")
    
class cat(Animal):
    def sound(self):
        print("The cat Meows")
        
A = Animal()
A.sound()

D = Dog()
D.sound()

C = cat()
C.sound()        