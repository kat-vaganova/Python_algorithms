# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать,
# задаются вводом с клавиатуры.

length = int(input('Enter the length of numbers: '))
number = int(input('Enter the number for search: '))

count = 0

for i in range(length):
    if i == number:
        count += 1

print(f'Your number has repeated {count}  times.')


