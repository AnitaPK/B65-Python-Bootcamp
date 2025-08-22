from datetime import datetime, timedelta

now = datetime.now()
print('now',now)

yesterday = now - timedelta(days=1)
print('yeasterday', yesterday)

tommarow = now + timedelta(days=1)
print('tommarow', tommarow)

formatted = now.strftime("%Y-%M-%D %H:%M:%S")
print('formatted', formatted)

DOB = datetime.strptime("2025-07-10","%Y-%m-%d")
print(DOB, 'DOB')

import time

print(time.time())
print(time.ctime())

# from time import time,ctime
# print(time)
# print(ctime())

time.sleep(5)
print("Hello world")

start =time.ctime()
for i in range(555_00_000):
    pass
end=time.ctime()
print('Execution time',start, end, 'seconds')

str = '       Wisdom sprouts       '
print(len(str), 'length of str')
print(len(str.strip()))
str = str.strip()
print(str.upper())
print(str.lower())
print(str.title())

str1 = 'Python is amazing'
str2 = str1.replace('amazing', 'fun')
print(str2)

fruitSTR = 'Apple Banana Mango'
print(fruitSTR)

fruitList = fruitSTR.split()
print(fruitList)

strFruit = ''.join(fruitList)
print(strFruit)

print(str1.startswith('p'))
print(str1.endswith('g'))

print(str1.find('Python'))
print(str1.find('is'))

print(str1.count('is'))

# Write a program to print current time every 5 seconds (3 times).
#  👉 Hint: time.sleep(5) in a loop

# time, datetime 

for i in range(3):
    time.sleep(5)        
    CURRENTtime = datetime.now().strftime('%H:%M:%S')
    print(CURRENTtime)