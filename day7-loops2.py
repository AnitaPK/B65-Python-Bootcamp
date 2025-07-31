fruits = ['Apple', 'Banana', 'Mango', 'Apple']  # list   mutable

for element in fruits:
    print("I like to eat ",element)
    print('length of ',element, ' is ',len(element))

colors = ('Red', 'Blue','Green')  # tuple   immutable

# diff between list and tuple 
for element in colors:
    print(element)
print('----------------')

numbers = {10, 20, 30 ,20}     # set  unique elements

for element in numbers:
    print(element**2)

print('----------------')

names = {'Tom', 'Jerry', 'Dick', 'Tom'}

for element in names:
    print(element)

# 1. create list of vegetable and iterate it 
# 2 create tuple of shades red color and iterate it
# 3 create set of friends name and iterate it
# 4 

user = {"name":'Arjun', "age": 20, "address":'Pune'}
print(type(user), "****type of user****")

for key in user:
    print(key)

for value in user.values():
    print(value)

for key, value in user.items():
    print('Your', key, ' is ', value)

# list []  , tuples ()   keys are the index keys start with 0 
#  , set {}   , dict {key:value} no sequence  

for i in range(10):
    print(i)
print('----------------')
for i in range(1, 11):
    print(i)

print('----------------')

for i in range(0,11,2):
    print(i)

userNames = ['Tom', 'Jerry', 'Dick']

for index, value in enumerate(userNames):
    print(index+1, '***', value)


# 4. find even numbers from 2 to 40 using range 
# 5. iterate subject dictionary using items()
    subject = {'Math':35, 'ENG':40, 'COMP': 30}

for key in subject:
    print(key)

for value in subject.values():
    print(value)

for key, value in subject.items():
    print(key, value)

cart = {
    "apple":3,
    "Banana":2,
    "milk":1,
    "Bread":2
}
price = {
    "apple":30,
    "Banana":10,
    "milk":50,
    "Bread":40
}
TotalPrice = 0

for index, value in cart.items():
    print(index, '*********',value)
    print(price[index])
    TotalPrice = TotalPrice + price[index] * value
    print(TotalPrice)

print(TotalPrice)

responces = ['YES','NO', 'MayBE','YES','NO','YES']   #index 0 start value

for element in responces:
    print(element)

for index , answer in enumerate(responces, start=1):
    print('responces', index, ' : ', answer)
