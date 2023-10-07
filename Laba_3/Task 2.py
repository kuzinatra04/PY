stroka = input('Введите строку: ')
newstroka = ''
count = 1

for i in range(len(stroka) - 1):
    if stroka[i] == stroka[i + 1]:
        count += 1
    elif stroka[i] != ' ':
        newstroka += stroka[i] + str(count)
        count = 1

newstroka += stroka[(len(stroka) - 1)] + str(count)

result = ''

for i in range(3):
    j = len(newstroka) - 1
    max = int(newstroka[j])
    key = newstroka[j - 1]
    k = j
    while j > 0:
        if max <= int(newstroka[j]):
            max = int(newstroka[j])
            key = newstroka[j - 1]
            k = j
        j -= 2
    result += key + str(max) + ' '
    newstroka = ''.join([newstroka[j] for j in range(len(newstroka)) if j != k and j != (k - 1)])

print(result)