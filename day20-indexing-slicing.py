str = 'Python'
print(str[0])
print(str[3])

print(str[-1])
print(str[-2])

fruits = ["Apple","Banana","Cherry","Mango","Orange"]
print(fruits[0])
print(fruits[-1])
# print(fruits[5])

numbers = (10,20,30,40)
print(numbers[0])
print(numbers[-1])


print(str[4:6])
print(str[:4])
print(str[:6:2])    

# 0 1 2 3 4 5 6
# P   t   o 

print(str[::-1])

print(fruits[0:4])
print(fruits[3:6])
print(fruits[::3])
print(fruits[-3::])
print(fruits[::-1])

print(numbers[:3])
print(numbers[::-1])

num = [1,2,3,4,5]
num[1:4] = [9,7,8]
print(num)

print(sorted(num,reverse=True))
print(num)


num1 = [65,87,23,45]
print(num1)
num1.sort(reverse=True)
print(num1)

words = ['is','Amazing', 'Python']

#print(words.sort()) #["Amazing", "is", "Python"]
# print(words.sort())

print(sorted(words, key=len))

student = [("Rahul",42),("Anjali",48),("Priya",32)]

print(sorted(student,key=lambda stud:stud[1]))

#  palindrome checker function 

def checkPlindrom():
    wordUser = input("Enter word")
    revWord = wordUser[::-1]
    if (wordUser == revWord):
        print("word is palindrom")
    else:
        print('NOT palindrom')
checkPlindrom()