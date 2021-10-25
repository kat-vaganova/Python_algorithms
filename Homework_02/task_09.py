# 9. Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр

from random import randint
max_sum = 0
sum_number = 0
i = 5
while i != 0:
    number = randint(1, 100)
    print(number)  # для проверки

    while number > 0:
        sum_number += number % 10
        number //= 10
        print(f'sum {sum_number}')

    if max_sum < sum_number:
        max_sum = sum_number
        print(f'The max sum  {max_sum}')

    i -= 1


print(f'The max sum of numbers {max_sum}')
