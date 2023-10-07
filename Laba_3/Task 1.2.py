from string import ascii_letters

stroka = 'Y4g2ke3A3BV'
print(stroka)
oldstroka = ''
for i in range(len(stroka) - 1):
    if stroka[i] in ascii_letters and stroka[i + 1] not in ascii_letters:
        oldstroka += stroka[i] * int(stroka[i + 1])
    elif stroka[i] in ascii_letters and stroka[i + 1] in ascii_letters:
        oldstroka += stroka[i]

if stroka[len(stroka) - 1] in ascii_letters:
    oldstroka += stroka[len(stroka) - 1]

print(oldstroka)