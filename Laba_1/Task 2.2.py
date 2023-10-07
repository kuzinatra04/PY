a = int(input('Введите кол-во чисел: '))

max_width = a
for i in range(1, a + 1):
    num_spaces = max_width - i
    print(' ' * num_spaces, end='')

    for j in range(1, i + 1):
        print(j, end='')

    for j in range(i - 1, 0, -1):
        print(j, end='')

    print()
