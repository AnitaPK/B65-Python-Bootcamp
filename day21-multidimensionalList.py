matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
print(matrix[2])

print(matrix[1][0])

print(matrix[2][2])
print([row[2] for row in matrix])

matrix[0][0] = 20
print(matrix)

matrix.append([22,33,44])
print(matrix)

for row in matrix:
    row.append(999)

print(matrix)

for row in matrix:
    row.pop()

print(matrix)

for row in matrix:
    for elmnt in row:
        print(elmnt*elmnt, end='  ')
    print()

