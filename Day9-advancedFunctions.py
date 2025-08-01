def greet(name='User'):
    print('Hello ', name)

greet()
# greet('Shrihari')

def send_email(to, subject='no subject', body=''):
    print('mail send to ', to)
    print('subject of email is ', subject)
    print('message from email is ',body)

send_email('admin@gmail.com', 'test subject', 'this is message for admin')
send_email('admin@gmail.com', body='****body message of the email*******')

def addition(*args):    # args is an tuple
    return sum(args)

print(addition(1,2,3))
print(addition(11,55,44,99,33,22,88))

def total_price(*args):
    return sum(args)

print(total_price(111,234,765))

def print_profile(**kwargs):           # kwargs is an Dictionary
    for key, value in kwargs.items():
        print('Your ', key, ' is', value)        



print_profile(name='Shrihari', age=30, city='Pune', grade='A+')
print('------------------------------')
def update_profile(userID,**kwargs):
    print('Your Id is', userID)
    for key, value in kwargs.items():
        print('Your ', key, ' is', value)

update_profile(1234567, name='Aditya', city='Mumbai', grade='A++')

# recursive function 

def demoFunction():
    demoFunction()

# for addition of first 10 natural numbers 

def additionOfNaturalNum(num):
    if(num == 0):
        return 0
    return num + additionOfNaturalNum(num-1)

print(additionOfNaturalNum(0))
print(additionOfNaturalNum(5))    # 5+4+3+2+1


# factorial of 5 10 

def factorialOfNumber(N):
    if N == 0:
        return 1
    if N == 1:
        return 1
    return N * factorialOfNumber(N-1)

print(factorialOfNumber(0), '0!')
print(factorialOfNumber(1),'1!')
print(factorialOfNumber(4),'4!') # 4*3*2*1
