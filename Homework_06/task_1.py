# 1. Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки)
# вставить в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность
# вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.
# Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof
# после каждой переменной, а проявили творчество, фантазию и создали универсальный
# код для замера памяти.


# Выбрана задача урока 2
#  3. Сформировать из введенного числа обратное
# по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

import sys
import random


def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


number = random.randint(100, 1000)
print(f'number = {number}')
show_size(number)
print()

# вариант 1

number_str = str(number)
renumber_1 = []
l = len(number_str)
for i in range(l-1, -1, -1):
    renumber_1.append(number_str[i])
print(f'renumber_1 = {"".join(renumber_1)}')

show_size(number)
show_size(number_str)
show_size(renumber_1)
show_size(l)

mem_1 = sys.getsizeof(number) + sys.getsizeof(renumber_1) + sys.getsizeof(number_str) + sys.getsizeof(l)
print(f'Затраты памяти под переменные в варианте 1: {mem_1} байт')
print()


# вариант 2

renumber_2 = ''.join(list(reversed(str(number))))
print(f'renumber_2 = {renumber_2}')

show_size(number)
show_size(renumber_2)
mem_2 = sys.getsizeof(number) + sys.getsizeof(renumber_2)
print(f'Затраты памяти под переменные в варианте 2: {mem_2} байт')
print()


# вариант 3

renumber_3 = 0
while number > 0:
    renumber_3 = renumber_3 * 10 + number % 10
    number //= 10
print(f'renumber_3 = {renumber_3}')

show_size(number)
show_size(renumber_3)
mem_3 = sys.getsizeof(number) + sys.getsizeof(renumber_3)
print(f'Затраты памяти под переменные в варианте 3: {mem_3} байт')
print()

# общий вывод:
# наименьшие затраты памяти в варианте 3, где использовались 2 переменные класса int
# наибольшие затраты памяти в варианте 1, где использовались 4 переменные классы: int, str, list
# наиболее "легкими" являются переменные класса int и оешения с их использованием
# number = 837
#  type= <class 'int'>, size= 28, object= 837
#
# renumber_1 = 738
#  type= <class 'int'>, size= 28, object= 837
#  type= <class 'str'>, size= 52, object= 837
#  type= <class 'list'>, size= 88, object= ['7', '3', '8']
# 	 type= <class 'str'>, size= 50, object= 7
# 	 type= <class 'str'>, size= 50, object= 3
# 	 type= <class 'str'>, size= 50, object= 8
#  type= <class 'int'>, size= 28, object= 3
# Затраты памяти под переменные в варианте 1: 196 байт
#
# renumber_2 = 738
#  type= <class 'int'>, size= 28, object= 837
#  type= <class 'str'>, size= 52, object= 738
# Затраты памяти под переменные в варианте 2: 80 байт
#
# renumber_3 = 738
#  type= <class 'int'>, size= 28, object= 837
#  type= <class 'int'>, size= 28, object= 738
# Затраты памяти под переменные в варианте 3: 52 байт
