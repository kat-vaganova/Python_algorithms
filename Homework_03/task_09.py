# 9. Найти максимальный элемент
# среди минимальных элементов столбцов матрицы.
import random
size = 4
# создаем матрицу
matrix = [[random.randint(1, 100) for _ in range(size)] for _ in range(size)]

# выводим на печать
for line in matrix:
    for el in line:
        print(f'{el:>4}', end='')
    print()
# находим мин эл в каждом столбце
min_column = [100] * len(matrix[0])
for line in matrix:
    for ind, el in enumerate(line):
        if min_column[ind] > el:
            min_column[ind] = el

print(('-' * len(matrix)*5))

# распечатываем мин эл и находим макс из них
max_el = 0
for el in min_column:
    print(f'{el:>4}', end='')
    if max_el < el:
        max_el = el
print()
print(f'максимальный элемент среди минимальных: {max_el}')
