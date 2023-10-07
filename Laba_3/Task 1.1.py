stroka = 'YYYYggkeeeAAABV'
print(stroka)
newstroka = ''
count = 1

for i in range(len(stroka) - 1):
    if stroka[i] == stroka[i + 1]:
        count += 1
    else:
        newstroka += stroka[i]
        if count != 1:
            newstroka += str(count)
        count = 1

newstroka += stroka[(len(stroka) - 1)]
if stroka[len(stroka) - 1] == stroka[len(stroka) - 2]:
    newstroka += str(count)

print(newstroka)