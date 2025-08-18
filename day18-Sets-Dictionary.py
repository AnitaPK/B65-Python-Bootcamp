fruits = {"Apple","Banana","Orange"}
print(fruits)
print(type(fruits))

setDemo = set()        #empty set
print(type(setDemo))

set1 = {1,3,4,6,9}
set2 = {2,3,4,5,7}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))     # {1,6,9}
print(set2.difference(set1))     # {2,5,7}
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))

fruits.add('Mango')
print(fruits)

fruits.update(["Papaya","Cherry"])
print(fruits)

fruits.remove('Papaya')
print(fruits)

fruits.discard("Che")
print(fruits)

fruits.clear()
print(fruits)

student = {
    "name":"Shrihari",
    "age":20,
    "division":"B",
    "subjects":["eng", 'Marathi',"Hindi",'Math']
}
for key,value in student.items():
    print(f"Your {key} is {value}")

print(student["name"])
print(student.get("age"))
student["age"] = 21
print(student.get("age"))
student["result"] = "Grade A"

for key,value in student.items():
    print(f"Your {key} is {value}")

student.popitem()

for key in student.keys():
    print(key)

student.pop('age')

for key in student.keys():
    print(key)

def add(x,y): return x+y
def sub(x,y): return x-y
def mul(x,y): return x*y
def div(x,y): return x/y

calculator = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

operation = '/'

result = calculator[operation](10,7)
print(result)


sentence = 'Apple Banana Apple Banana Orange Banana'
words = sentence.split()
print(words)
outputCount = {}

for word in words:
    outputCount[word] = outputCount.get(word , 0) + 1

print(outputCount)

numbers = [1,2,2,3,4,5,6,6,6,6]
print(numbers)
num_sets = list(set(numbers))
print(num_sets)