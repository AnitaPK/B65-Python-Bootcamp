# while() 

# 1 -- 5

x = 1
while x <=5:
    print(x)
    x+=1

i = 1
while i <= 10:
    print('17 * ',i, '=', 17*i)
    i+=1
print(i)

abc = range(5)
print(abc)

for x in range(1,6):
    print(x)

for i in range(1,11):
    print('17 * ', i, ' = ', 17*i)

fruits = ['Apple','Mango','chickoo']

for fruit in fruits:
    print("I like to eat",fruit)

str = 'PYTHON13'

for ch in str:
    print(ch)
print('************')
for m in range(1, 11):
    print(17 * m)



for v in range(10):
    if v == 5:
        break
    print(v)
print('______________')
for y in range(10):
    if(y == 5):
        continue
    print(y)
print('*********')
for z in range(10):
    if(z==5):
        pass
    print(z)

# infine loop 
def infineLoop():
    while True:
        print('Leaning PYTHON')

strInput = input('Enter string : ')

for ch in strInput:
    print(ch)
print('---------------------')
num1 = int(input("enter Number : "))
result = 0
for k in range(1, num1+1):
    result = result+k
print(result, 'result from for loop')

resultWhile = 0
l = 1
while l <=num1:
    resultWhile = resultWhile + l
    l+=1 
print(resultWhile,'result from while loop')
print('--------------')
for i in range(1,11):
    if(i%2 == 0):
        continue
    print(i)