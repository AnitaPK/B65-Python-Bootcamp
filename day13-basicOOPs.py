class ClassName:
    pass
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def getPropertise(self):
        print(self.brand)
        print('Color of Car : ',self.color )    

    def start(self):
        print('Car started')
    
    def stop(self):
        print('By using break')

ALTO800 = Car('Red', 'maruti')

print(ALTO800.start() ,'Alto')
print(ALTO800.getPropertise(),'Alto')

porsche911 = Car('White','Porsche')

print(porsche911.start(), 'porsche')
print(porsche911.getPropertise(), 'porsche')

mustang = Car('Black','Ford')
print(mustang.start(), 'mustang')
print(mustang.getPropertise(), 'mustang')
print('to stop a car you have to use break', mustang.stop())


# create a class for Student and create any 2 students from that class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getInfo(self):
        print(self.name, ' :::  ', self.age)

shrihari = Student('Shrihari', 10)
aditya = Student('Aditya', 15)

print(shrihari.getInfo())
print(aditya.getInfo())