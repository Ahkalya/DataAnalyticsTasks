class Circle:
    def area(self):
        print("Area = π × r²")

class Rectangle:
    def area(self):
        print("Area = length × width")

class Triangle:
    def area(self):
        print("Area = ½ × base × height")

def print_area(shape):
    shape.area()


c = Circle()
r = Rectangle()
t = Triangle()

print_area(c) 
print_area(r)   
print_area(t)  
