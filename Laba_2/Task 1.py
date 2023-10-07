def Pascal(n):
    number = [[1]]

    for i in range(1, n + 1):
        pere = [1] * (i + 1)
        for j in range(i + 1):
            if not (j == 0 or j == i):
                pere[j] = number[i - 1][j - 1] + number[i - 1][j]

        number.append(pere)

    return number


n = int(input('Введите кол-во строк: '))

for i in range(len(Pascal(n))):
    print(Pascal(n)[i])

