# 3. В массиве случайных целых чисел
# поменять местами минимальный и максимальный элементы.
import random

numbers = [random.randint(1, 100) for _ in range(10)]
print(numbers)

min_el = numbers[0]
max_el = numbers[0]

for ind, el in enumerate(numbers):
    if el < min_el:
        min_el = el
        min_ind = ind
    if el > max_el:
        max_el = el
        max_ind = ind
print(f' мин число {min_el}  с индексом {min_ind},'
      f'макс число {max_el}  с индексом {max_ind}')
numbers[min_ind] = max_el
numbers[max_ind] = min_el
print(numbers)
