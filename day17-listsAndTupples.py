fruits = ['Apple', 'Mango','Banana']
student = ['John', 'Jerry', 'Tom', 'Dick']
marks = [45, 65, 90, 94,56]
user = ['Shrihari', 20, {"city":"pune", "State":"MH"}]

print(fruits)
# fruits[3] = 'Cherry'
# print(fruits)

fruits.append('Watermelon')
print(fruits)

fruits.extend(["Cherry", "Papaya"])
print(fruits)

fruits.insert(1, 'Pinnaple')
print(fruits)

fruits.remove('Cherry')
print(fruits)

fruits.pop(2)
print(fruits)

print(marks)
marks.sort(reverse=True)
print(marks)

# fruits.sort()
# print(fruits)
# fruits.reverse()
# print(fruits)

sortedFruits = sorted(fruits)
print(sortedFruits)
print(fruits)

print(fruits.count('Apple'))

newFruitList = fruits.copy()
print(newFruitList, 'New list')
print(fruits, 'old List')

fruits.append('Cherry')
print(newFruitList, 'New list after append')
print(fruits, 'old List after append on new list')



newFruitList.clear()
print(newFruitList)

employee = ("John Doe", 30, 'Pune')

print(employee[1])
# employee[1] = 40
print(employee)

(firstName, age, city) = employee
print(city)

matrixTuple = ((2,3),(7,8))

print(matrixTuple[1][0], 'value of row2and col1')