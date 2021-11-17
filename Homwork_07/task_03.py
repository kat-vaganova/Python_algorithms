# 3. Массив размером 2m + 1, где m — натуральное число,
# заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

""" Находим середнее значение для элементов списка,
сравнивая каждый элемент с ним находим тот чье отличие минимально
это и есть медиана"""

import random


m = random.randint(2, 8)
array = [random.randint(0, 50) for _ in range(2*m + 1)]
print(array)


def looking_median(array):
    middle = (min(array) + max(array)) // 2
    print('middle', middle)
    median = None
    dif = max(array) - middle
    for el in array:
        if el == middle:
            median = el
        elif el < middle:
            if dif > middle - el:
                dif = middle - el
                median = el
        elif el > middle:
            if dif > el - middle:
                dif = el - middle
                median = el

    return median


print('median', looking_median(array))
