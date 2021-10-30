# 8. Матрица 5x4 заполняется вводом с клавиатуры,
# кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу

size = 4
matrix = [[] for _ in range(size)]

for line in matrix:
    sum_line = 0
    for i in range(size):
        num = int(input('Enter the numbers for matrix: '))
        line.append(num)
        sum_line += num
    line.append(sum_line)

for line in matrix:
    for el in line:
        print(f'{el:>4}', end='')
    print()



