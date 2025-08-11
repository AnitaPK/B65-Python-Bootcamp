class Book:
    def __init__(self, name,author):
        self.name = name
        self.author =author
    def __str__(self):
        return f"{self.name} by {self.author}" 
    def __repr__(self):
        return f"Book({self.name}, {self.author})"


B1 = Book('BasicOfPython', 'John Doe')

print(str(B1))
print(repr(B1))

class Vector:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y+ other.y)
    

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
v1 = Vector(2,3)
v2 = Vector(4,5)
v3 = Vector(9,8)
firstV = v1 + v2 
print(str(firstV))
finalV = firstV + v3
print(str(finalV))

class Rectangle:
    def __init__(self, length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

    def __repr__(self):
        return f"Rectangle({self.length}, {self.width})"

    def __str__(self):
        return f"Rectangles length is{self.length}, and width is {self.width}."

    def __add__(self, other):
        return self.area() + other.area()

    def  __eq__(self, other):
        return self.area() == other.area()

r1 = Rectangle(10,6)
r2 = Rectangle(4,9)

print(str(r1))
print(repr(r1))
print(r1+r2, "Total area")
print("Both are same?", r1 == r2 )



