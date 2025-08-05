

def greet():
    name1 = 'Shrihari'
    print('Hello', name1)

greet()


userName = 'Amit'
def greetOne():
    print('Hello', userName)

greetOne()

count = 0
def counterIncreament():
    global count
    count = count+1


def counterDecreament():
    global count
    count = count-1

print(count, 'before function call')     #  0

counterIncreament()
print(count, 'after function call')      #   1

count =count+1
print(count, 'increament outside the function')   # 2

counterDecreament()
print(count, 'decreament ')


counterIncreament()
print(count, 'after function call')      # 3

counterIncreament()
print(count, 'after function call')      # 4


def outer():
    message = 'Hey Hello whats going on!!!!'
    print(message)

    def inner():
        nonlocal message
        print(message)

    inner()

outer()

attempts = 0
def login():
    global attempts
    attempts += 1
    print('Login attemp count', attempts)


login()

login()

def counter1():
    countNumber = 0
    def increament():
        nonlocal countNumber
        countNumber+=1
        return countNumber
    return increament


c1 = counter1()

print(c1())
print(c1())


