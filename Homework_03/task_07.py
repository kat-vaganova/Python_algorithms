# 7. В одномерном массиве целых чисел
# определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны),
# так и различаться.
import random
numbers = [15, 31, 15, 41, 16]
# numbers = [7, 39, 26, 88, 99, 96, 67, 100, 43, 49]
# numbers = [random.randint(1, 100) for _ in range(10)]
print(numbers)

min_el_1 = numbers[-1]
min_el_2 = numbers[0]

for el in numbers:
    if el < min_el_1:
        min_el_2 = min_el_1
        min_el_1 = el
    elif el < min_el_2:
        min_el_2 = el

print(f'наименьшиу элементы: {min_el_1}, {min_el_2}')

