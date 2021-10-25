# 3. Сформировать из введенного числа обратное
# по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

import random

number = random.randint(1, 100)
print(f'number = {number}')
renumber = 0

while number > 0:
    renumber = renumber * 10 + number % 10
    number //= 10

print(f'renumber = {renumber}')

