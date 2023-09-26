a = int(input('Введите кол-во чисел: '))

#Вариант 1
for i in range(1, a + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

#Вариант 2
st = ''

for i in range(1, (a + 1)):
    st += str(i)
    print(st)