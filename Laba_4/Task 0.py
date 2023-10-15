stroka = [12, 35, 45, 23, 34, 10, 67, 65, 45, 33, 85]
newstroka = []
for i in range(len(stroka) - 1):
    if stroka[i] < stroka[i + 1]:
        newstroka.append(stroka[i + 1])

print(newstroka)