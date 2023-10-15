stroka1 = [12, 34, 45, 23, 34, 10, 67, 65, 45, 34, 85]
stroka2 = [43, 56, 87, 12, 7, 45, 76, 34, 23, 10]
count = 0
stroka1 = sorted(stroka1)

i = 0
while i < len(stroka1):
    a = stroka1.count(stroka1[i])
    j = 0
    while j < len(stroka2):
        if stroka1[i] == stroka2[j]:
            count += 1
            j = len(stroka2)
        j += 1
    i += a

print(count)