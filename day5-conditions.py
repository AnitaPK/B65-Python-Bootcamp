temperature = 10

if temperature > 20:
    print('Today is hot outside!!!')
print('Every Day is fun day')

age = 18
if age >= 18:
    print('You can vote')
else:
    print('Can not vote')


# find the number is positive or negetive or Zero
number = 0
if number > 0:
    print('Number is positive')
elif number < 0:
    print('Numberis negetive')
else:
    print('number is zero')

# grade calculator 
# A    >=80    B   60-80     C    40-60       F   >40

grade = 14

if grade >= 80:
    print('Grade is A')
elif grade < 80 and grade >= 60:
    print('Grade is B')
elif grade < 60  and grade >= 40:
    print('Grade is C')
else:
    print('Grade is F')

age = 45
nationality = 'American'

if age >= 18:
    if nationality == 'Indian':
        print('You can VOTE')
    else:
        print('You can not VOTE')
else:
    print('You can not VOTE because of your age')

if age>= 18 and nationality == 'Indian':
    print('You can VOTE')
else:
    print('You can not VOTE')

is_logged_in = True
is_admin = False

# if is_logged_in == True and is_admin == True:
if is_logged_in and is_admin:
    print("Welcome Admin") #if both are true
elif is_logged_in and not is_admin:
    print("Welcome User") #if logged in but not admin
else:
    print("Please log in") # otherwise



if is_logged_in:
    if is_admin:
        print("Welcome Admin") #if both are true
    else:
        print("Welcome User") #if logged in but not admin
else:
    print("Please log in") # otherwise

# n1 = input('Number One : ')
# n2 = input('Number Two : ')
# n3 = input('Number Three : ')
# if n1 >n2 and n1>n3:
#     print(n1, ' is grater')
# elif n2>n1 and n2 > n3:
#     print (n2, ' is grater...')
# else:
#     print (n3, ' is greater ...')

number1 = int(input("Enter number to check even or odd"))
if number1 % 2 == 0:
    print(number1,' is even')
else:
    print(number1,' is odd')
