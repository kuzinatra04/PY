mnog1 = set(input('Введите первое множество через пробел: ').split())
mnog2 = set(input('Введите второе множество через пробел: ').split())
if mnog1 == mnog2:
    print('False')
else:
    print(mnog1.issubset(mnog2))