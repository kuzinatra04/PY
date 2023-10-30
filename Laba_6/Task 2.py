with open('input_2.txt') as file:
    spisok = (file.read()).split('\n')

for i in range(len(spisok)):
    spisok[i] = int(spisok[i])

spisok.sort()

with open('output_2.txt', 'w') as file:
    for i in range(len(spisok)):
        print(spisok[i], file=file)