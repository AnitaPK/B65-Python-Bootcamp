print('Hello World')

name = 'Wisdom Sprouts'

Name = "John Doe"

print(name)

# integer 
age = 20
year = 2025
num = 0
num1 = -34
strNumber = '234'
# float 
sallary = 123456789.00
price = 99.99

# complex 
num3 = 2+5j 


# str

NAME = 'Virat Kohli'

# Boolean  0 1 bool 
isActive = True
isLoggedIn =False

# NoneType
X = None

# list 
fruits = ['Apple', 'Mango','Banana','Apple']

#set 
fruitsSet =  {'Apple', 'Mango', 'Banana'}

#tuple
coordinate = (5.456789,78456.789)

#range()
numberSet = range(10)     # [0,1,2,3,4,..., 9]

#dict dictionary  (objects) key value pair
userProfile = {"name":'John Doe',"DOB":'2000-12-31',"city":'Pune', "sallary":12345678.56}



print(type(NAME))
print(type(sallary),'sallary')
print(type(age),'age')
print(type(isActive),'isActive')
print(type(X),"X")
print(type(fruits), 'fruits')
print(type(fruitsSet),'fruitsSet')
print(type(coordinate), 'coordinate')
print(type(numberSet), 'numberSet')
print(type(userProfile),'userProfile')

numberFromStr = int(strNumber)

print(numberFromStr ,'numberFromStr', type(numberFromStr))
print(strNumber,'strNumber',type(strNumber))

print(price,'price',type(price))
priceInteger = int(price)
print(priceInteger,'priceInteger', type(priceInteger))
print(sallary,'sallary',type(sallary))
sallarySTR = str(sallary)
print(sallarySTR, "sallarySTR", type(sallarySTR))


# firstName = input('Enter forst name')
# print("Welcome to our virtual session", firstName)
# print(type(firstName))

valueFromUser = input('Enter value')
print(valueFromUser, 'at start',type(valueFromUser))
valueAfterConvert = float(valueFromUser)
print(valueAfterConvert, 'after', type(valueAfterConvert))