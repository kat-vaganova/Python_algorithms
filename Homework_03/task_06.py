# 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

numbers = [random.randint(1, 100) for _ in range(80)]
print(numbers)


def sum_el(numbers):
    min_el = numbers[0]
    max_el = numbers[0]
    max_ind = None
    min_ind = None
    summa = 0
    for ind, el in enumerate(numbers):
        if el < min_el:
            min_el = el
            min_ind = ind
        if el > max_el:
            max_el = el
            max_ind = ind
    print(f"Наибольшее значение: {max_el} наименьшее значение: {min_el}")

    if min_ind <= max_ind:
        print(f'Искомый массив: \n{numbers[min_ind+1:max_ind]}')
        for el in numbers[min_ind+1:max_ind]:
            summa += el
    else:
        print(f'Искомый массив: \n{numbers[max_ind+1:min_ind]}')
        for el in numbers[max_ind+1:min_ind]:
            summa += el
    return summa


print(f'сумма элементов {sum_el(numbers)}')
