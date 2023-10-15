spisok = input().split()
dict = {}

while spisok != []:
    count = spisok.count(spisok[0])
    dict.update({spisok[0]:count})
    a = spisok[0]
    for i in range(count):
        spisok.remove(a)

print(dict.values())

#Для проверки
#abc bcd abc abd abd dcd abc
#aaa bbb ccc
#abc abc abc


#Другая версия кода, но работает дольше при огромных списках,
    #так как перебирает повторные

#spisok = input().split()
#dict = {}

#i = 0
#while i < len(spisok):
    #a = spisok.count(spisok[i])
    #dict.update({spisok[i]:a})
    #i += 1

#print(dict.values())
