# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

numbers = range(2, 99)
denominators = range(2, 9)

for den in denominators:
    i = 0
    for num in numbers:
        if num % den == 0:
            i += 1
    print(f'{i} чисел кратны {den}')



