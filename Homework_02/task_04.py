# 4. Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.

n = int(input('Enter the number: '))

summa = 0
for i in range(n):
    summa += 1 / (-2) ** i

print(f"summa {summa}")
