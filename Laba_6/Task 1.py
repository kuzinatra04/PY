with open('input_1.txt') as file:
    spisok = (file.read()).split()

pr = 1
for i in range(len(spisok)):
    pr *= int(spisok[i])

with open('output_1.txt', 'w') as file:
    print(pr, file=file)