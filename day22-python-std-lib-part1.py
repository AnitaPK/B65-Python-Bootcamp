import os 

print(os.name)

print(os.getcwd())

# os.makedirs('Day22')
# os.rmdir('Day22')

# print(os.listdir('.'))
# os.environ()

import sys
# print(sys.version)
# print(sys.platform)

# print(sys.argv)
# sys.exit()

import math

# print(math.pi)
# print(math.sqrt(256))
# print(math.factorial(10))
# print(math.sin(math.pi/2))
# print(math.ceil(10.2))
# print(math.floor(10.2))

import random

print(math.ceil(random.random() *10000))

print(random.randint(1000,9999))

print(random.sample(range(10), 4))

print(random.choice(['Python','Java','DotNet']))

# Write a script that checks the total size of files inside a directory and prints the top 5 largest files.
# Hint: Use os.path.getsize() and sorting

def getLargestFiles(path):
    files = []

    for f in os.listdir(path):
        filePath = os.path.join(path,f)
    
        if os.path.isfile(filePath):
            size = os.path.getsize(filePath)
            files.append((f, size))

    files.sort(key=lambda x:x[1], reverse=True)

    print("5 files", path)
    for name, size in files[::6]:
        print(name, size)
getLargestFiles('.')

# Simulate rolling two dice until you get a double six. Print how many tries it took.
# Hint: Use random.randint(1,6).
count = 0
while True:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    count+=1
    print(dice1,"  ", dice2)
    if dice1 == 6 and dice2 ==6:
        print("got double 6 !!! in ", count, "tries")
        break