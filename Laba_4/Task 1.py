stroka = [12, 35, 45, 23, 34, 10, 67, 65, 45, 33, 85]

a = stroka.index(min(stroka))
b = stroka.index(max(stroka))
stroka[a], stroka[b] = stroka[b], stroka[a]

print(stroka)