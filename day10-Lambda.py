def squareOfX(x):
    return x*x

squareXValue = squareOfX(4)
print(squareXValue, 'squareOfX')

Xsquare = lambda x: x*x

print(Xsquare(4), 'Xsquare')

def additon(a,b):
    return a+b

add4_5 = additon(4,5)
print(add4_5, 'add4+5','addition')

addNUM = lambda a,b: a+b

add6_7 = addNUM(6,7)
print(add6_7,'add6_7')

# map on list 

numbersList = [1,2,3,4,5]
def SQOfListItems(listOne):
    for x in listOne:
        return x*x

outputListSquare = list(map(lambda j: j*j, numbersList))
print(numbersList,'numbersList')
print(outputListSquare,'outputListSquare')

inputMarks = [43, 56, 87, 65, 90]
outputPercentOfMarks = list(map(lambda m: 100 * m / 120,inputMarks))

# 120 - 43
# 100 - ?
# 600 - ___ 
# 100 - ?
print(inputMarks)
print(outputPercentOfMarks)

numbers = [10,15,20,25,30,35,40]

# find even numbers 
evenNumbers = list(filter(lambda n:n%2==0, numbers))
print(numbers,'numbers')
print(evenNumbers,'evenNumbers')

# find odd numbers
oddNumbers = list(filter(lambda n:n%2 !=0,numbers))
print(oddNumbers,'oddNumbers')

from functools import reduce

sumOfAllNumbers = reduce(lambda a,b: a+b , numbers)
print(sumOfAllNumbers,'sumOfAllNumbers')

sumOfAllMarks = reduce(lambda a,b:a+b, inputMarks)
print(sumOfAllMarks, 'sumOfAllMarks')

def findPercent(listInput):
    totalMarks = reduce(lambda a,b :a+b, listInput)
    return totalMarks * 100 / 600

jimmy = [34,56,76,83,61]
gill = [98,83,49,91,79]
print(findPercent(jimmy), 'percent of jimmy')
print(findPercent(gill), 'percent of gill')

wordList = ['Python','is','fun','to','learn']

strOne = reduce(lambda x, y : x+' '+y, wordList)
print(strOne)

stud_info = [('Ram', 88),('Sham',67), ('Meera',93)]
print(stud_info, 'stud_info')

sortStudent = sorted(stud_info, key=lambda x: x[1])
print(sortStudent, 'sortStudent')