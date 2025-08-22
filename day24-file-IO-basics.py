# f = open('demoDay24.txt','w')

# f.write('Hello , this is file demo Day24')

# f.close()

f1 = open('demoDay24.txt', 'r')

contentF1 =f1.read()
print(contentF1)
f1.close()

f2 = open('demoDay24.txt','r')
print(f2.readline())
print(f2.readlines())

f2.close()

f3 = open('demoDay24.txt', 'a')
f3.write("This is last line")
f3.close()

f4 = open('demoDay24.txt', 'r')

contentF4 =f4.read()

print(contentF4)
print('*********************')


with open('demoDay24.txt','r') as f5:
    # contentF5 = f5.read()
    # print(contentF5)
    for line in f5:
        print(line.strip())

with open('day24Demo.bin','wb') as f6:
    f6.write(b'Hello in day24Demo binary ')

with open('day24Demo.bin','r') as f7:
    contentF7 = f7.read()
    print(contentF7)