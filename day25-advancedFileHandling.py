f = open('day25text.txt', 'w')

f.write('Hello , This is first line...\n  , this is file demo Day25')
f.close()


f1 = open('day25text.txt', 'r')

data = f1.read()
print(data)
f1.close()


with open('day25text.txt', 'r') as f3:
    print('************')
    print(f3.readline())
    print('************')

    print(f3.readlines())
    # xyz = f3.read()
    # print(xyz)
    print('************')

with open('day25text.txt', 'r') as f4:
    for line in f4:
        print(line.strip())

print('************')

dataLang = ['Python', 'Java', 'C++', 'GoLang']

with open('language.txt', 'w') as f5:
    for elemnt in dataLang:
        f5.write(elemnt + "\n")

with open('language.txt', 'r') as f6:
    for line in f6:
        print(line.strip())

import json
student = {"Name":"Shrihari","Age":20,"grade":"A+"}

with open('dictSave.json','w') as f7:
    json.dump(student,f7)

with open('dictSave.json', 'r') as f8:
    data = json.load(f8)
    print(data['Name'])

with open('dataPython.txt', 'r') as f9:
    for line in f9:
        if 'Python' in line:
            print(line)