class BankAccount:
    def __init__(self, Balance):
        self.balance = Balance 

    def withdraw(self, amt):
        if amt > self.balance:
            raise ValueError("Insuffiecient Fund")
        self.balance -= amt
        return self.balance
    def deposite(self, amt):
        if amt <= 0:
            raise ValueError('Invalid amount')
        self.balance = self.balance + amt
        return  self.balance

account456234 = BankAccount(5000)

print(account456234.withdraw(1000))

try:
    account456234.deposite(20000)
    account456234.withdraw(10000)
    account456234.deposite(-876543)
except ValueError as error:
    print('Transaction failed', error)
finally:
    print('Thank you')

class invalidAgeError(Exception):
    """This will raise when age in not in range """
    pass


class Person:
    def  __init__(self, name):
        self.name = name
    def set_age(self, age):
        if 0 > age < 130:
            raise ValueError('please add correct age')
        self.age = age
    
    def getInfo(self):
        return f'Your name is {self.name} age is {self.age} '

AMAR = Person('Amar')
try:
    AMAR.set_age(60)

except ValueError as e:
    print("Error", e)

print(AMAR.getInfo())

class InvalidMarksError(Exception):
    """ Invalid marks """
    pass

class Student:
    def __init__(self, name, data):
        self.name = name
        for key, marks in data.items():
            if 0< marks >100:
                raise InvalidMarksError("Marks should be in range")
    def getResult():
        pass

VIRAJ = Student('Viraj',{'math':50, 'english':70})
HARI = Student('Hari',{'marathi':60,'math':50, 'english':70})
