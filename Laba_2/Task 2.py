from math import pow

depth = int(pow(2, float(input('Введите степень 2: '))))

pascal = []
for _ in range(depth):
    a = [0] * depth
    pascal.append(a)

for i in range(len(pascal)):
    pascal[i][0] = 1
    pascal[i][i] = 1

for i in range(1, len(pascal)):
    for j in range(1, len(pascal[i])):
        pascal[i][j] = (pascal[i - 1][j - 1] + pascal[i - 1][j]) % 2

for i in range(len(pascal)):
    for j in range(len(pascal[i])):
        if pascal[i][j] == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()
