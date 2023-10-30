spisok = []
with open('input_3.txt', encoding='utf-8') as file:
    while True:
        line = file.readline()
        if not line:
            break
        spisok.append(line.strip())

min = spisok[0][len(spisok[0]) - 1]
minin = 0
max = spisok[0][len(spisok[0]) - 1]
maxin = 0
for i in range(1, len(spisok)):
    if min > spisok[i][len(spisok[i]) - 1]:
        min = spisok[i][len(spisok[i]) - 1]
        minin = i
    if max < spisok[i][len(spisok[i]) - 1]:
        max = spisok[i][len(spisok[i]) - 1]
        maxin = i

with open('output_3_min.txt', 'w', encoding='utf-8') as file:
    print(spisok[minin], file=file)

with open('output_3_max.txt', 'w', encoding='utf-8') as file:
    print(spisok[maxin], file=file)