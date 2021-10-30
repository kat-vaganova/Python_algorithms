# 4. Определить, какое число в массиве встречается чаще всего.
import random

numbers = [random.randint(1, 10) for _ in range(25)]
print(numbers)

num_set = set(numbers)

quantity = 0
max_quantity = 0
dict = {}
most_common = 0

for el in num_set:
    quantity = numbers.count(el)
    dict[el] = quantity
    if quantity > max_quantity:
        max_quantity = quantity
        most_common = el

print(dict)
print(f'в массиве встречается чаще всего число: {most_common} - {max_quantity} раз')


