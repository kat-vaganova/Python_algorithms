# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.


import random

size = 10
array = [random.randint(-100, 100) for _ in range(size)]
random.shuffle(array)
print(array)


def babble_sort(array):

    for a in range(len(array)):

        for i in range(len(array) - (a+1)):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        print(array)


babble_sort(array)
print(array)

