# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import Counter

# создаем словарь с наименованиями фирм и поквартальной прибылью
count = int(input("Enter the count of company "))
all_profit = 0
companies = Counter()
i = 1
while count >= i:
    name = input(f'Enter the name of {i} company ')

    x = 1

    year_profit = 0
    while x <= 4:
        profit_value = int(input(f'Enter the profit of {i} company for {x} quarter '))
        all_profit += profit_value
        year_profit += profit_value
        x += 1

    companies[name] = year_profit
    i += 1

# print(companies)

# определяем среднюю прибыль
middle_profit = all_profit/count
print(f'Средняя прибыль для компаний составила: {round(middle_profit, 2)}')

# выявляем фирмы с прибылью больше и меньше средней
more_middle = [key for key, value in companies.items() if value > middle_profit]
less_middle = [key for key, value in companies.items() if value < middle_profit]
print(f'Предприятия, чья годовая прибыль выше средней: {more_middle}')
print(f'Предприятия, чья годовая прибыль ниже средней: {less_middle}')
