def hello_user():
    print('Hello User')

hello_user()
# call invoke

def greetUser(name):
    print('Happy New Year', name)

greetUser('Shrihari')
greetUser('Meera')
greetUser('John')

# hello_user()
# hello_user()
# hello_user()
# hello_user()

def addTwoNum(n1=1,n2=1):
    print(n1+n2)
    return n1+n2

outputWithoutArgu = addTwoNum()
print(outputWithoutArgu,'outputWithoutArgu')

outputOfaddTwoNum = addTwoNum(4,5)
print(outputOfaddTwoNum, 'outputOfaddTwoNum')

# num1 = int(input("Enter Number 1 "))
# num2 = int(input("Enter Number 2 "))

# outputOfUserInput = addTwoNum(num1,num2)
# print(outputOfUserInput,'outputOfUserInput')

def student(name,grade):
    print(name, ' you got grade ', grade)

student('Arjun', 'B+')

student(grade='A',name='Krishna')
student('A+','John')  # sequence matters add with parameter