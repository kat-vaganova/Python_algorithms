# 2. Посчитать четные и нечетные цифры введенного натурального числа
# Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

count_even = 0
count_not_even = 0
number = input('Enter the number: ')
for i in number:
    if int(i) % 2 == 0:
        count_even += 1

    else:
        count_not_even += 1

print(f'Even numbers: {count_even}')
print(f'Not even numbers: {count_not_even}')
