numberList = [1,2,3,4,5,6,7,8,9,10]
print(numberList)
squareNumberList = [n**2 for n in numberList]
print(squareNumberList)

evenNumberList = [n for n in numberList if n%2==0]
print(evenNumberList)

wordList = ["apple",'Mango','banana']
capsListFruit = [fruit.upper() for fruit in wordList]
print(capsListFruit)

matrix = [[1,2,10],[3,4,11,15],[5,6,12]]

flattenList = [n for row in matrix for n in row]
print(flattenList)



numsSquare = (n**2 for n in range(5))
print(numsSquare)

for num in numsSquare:
    print(num)

def simple_generatorExpression():
    yield 'one'
    yield 'Two'
    yield 'three'

for v in simple_generatorExpression():
    print(v)

def countDown(n):
    while n>=0:
        yield n
        n = n-1

for v in countDown(10):
    print(v)

def readFile(file):
    with open(file) as F:
        for line in F:
            yield line.strip()

for line in readFile('progOne.py'):
    print(line)