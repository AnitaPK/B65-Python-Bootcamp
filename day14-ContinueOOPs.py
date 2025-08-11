class Vehicle:
    def start():
        print("Car starts...")

class Car(Vehicle):
    def play_music():
        print("Press play button on screen")

class Animal():
    def speak(self):
        print("animal Speaks")

class Dog(Animal):
    def bark(self):
        print('Dog Barks')

tommy = Dog()

tommy.speak()
tommy.bark()

class Employee():
    def fullName(self):
        print('This is your name : ')

class Manager(Employee):
    def baseSalary(self):
        print('This is your base salary')

John = Manager()
John.fullName()
John.baseSalary()

class Animal():
    def animal_sound(animal):
        animal.sound()

class Dog(Animal):
    def sound(self):
        print("BARK")

class Cat(Animal):
    def sound(self):
        print("MEOW")

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())

class Vehicle:
    def drive(self):
        return "moving"

class Car(Vehicle):
    def drive(self):
        return "Driving"

class Bike(Vehicle):
    def drive(self):
        return "Ride"

Honda = Car()
Ducati = Bike() 

print('Honda : ', Honda.drive())

print('Ducati : ', Ducati.drive())


class Person:
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    def setNewName(self,newName):
        if isinstance(newName,str) and newName.strip():
            self.__name = newName
        else:
            print("invalid")    
            # return self.__name

john = Person('John Doe')

print(john.getName(), 'Created ')
john.setNewName('johhhn Doeeeee')

print(john.getName() , 'after change')

class BankAccount:
    def __init__(self):
        self.__balance = 0
    def deposite(self, amt):
        self.__balance+= amt
    def checkBalance(self):
        return self.__balance

johnDoe = BankAccount()
print(johnDoe.checkBalance(), 'before deposite / first time')

johnDoe.deposite(1000)

print(johnDoe.checkBalance(), 'after deposite')

from abc import  ABC, abstractmethod

class Vehical(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehical):
    def start_engine(self):
        print("Engine started")
    
maruti800 = Car()
maruti800.start_engine()