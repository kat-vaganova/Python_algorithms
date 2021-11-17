# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random
from operator import lt

array = [random.randint(0, 50) for _ in range(20)]
print(array)


def merge_sort(array):

    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge_list(left, right)


def merge_list(left, right):
    # print(left, right)
    i, j = 0, 0
    result = []

    while i < len(left) and j < len(right):
        if lt(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # после сортировки могут остаться неотсортированные значения
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


print(merge_sort(array))
