count = int(input('Введите кол-во городов: '))
spisok = set()
for i in range(1, count + 1):
    a = input(f'Введите город номер {i}: ')
    spisok.add(a)

gorod = input('Введите неназванный город: ')

if gorod in spisok:
    print('REPEAT')
else:
    print('OK')