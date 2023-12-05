import csv
import matplotlib.pyplot as plt

#Чтение данных из CSV-файла
with open('passengers.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Пропуск заголовка
    data = list(reader)

#Преобразование данных в числовой формат
passengers = [int(row[1]) for row in data]

#График пассажиропотока за все время
plt.figure(figsize=(10, 6))
plt.plot(passengers)
plt.title('Пассажиропоток за все время')
plt.xlabel('Месяцы')
plt.ylabel('Кол-во пассажиров')
plt.show()

#Распределение пассажиров по месяцам в 1951-1955 гг.
year_month = [row[0] for row in data]
years = set([int(x.split('-')[0]) for x in year_month])
selected_years = [year for year in years if 1951 <= year <= 1955]

selected_data = [row for row in data if int(row[0].split('-')[0]) in selected_years]
months = [row[0] for row in selected_data]
passengers_monthly = [int(row[1]) for row in selected_data]

plt.figure(figsize=(10, 6))
plt.bar(months, passengers_monthly)
plt.title('Распределение пассажиров (1951-1955)')
plt.xlabel('Месяцы')
plt.ylabel('Кол-во пассажиров')
plt.show()
