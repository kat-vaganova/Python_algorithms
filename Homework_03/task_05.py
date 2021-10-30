# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный»
# и «максимальный отрицательный». Это два абсолютно разных значения.


import random

numbers = [random.randint(-10, 10) for _ in range(10)]
print(numbers)


def is_max(num):
    temp_dict = {ind: num[ind] for ind in range(len(num)) if num[ind] < 0}
    max_el = -10
    for value in temp_dict.values():
        if value > max_el:
            max_el = value
    return {f'Позиция в массиве {key}': f'искомое число {value}' for key, value in temp_dict.items() if
            value == max_el}


print(is_max(numbers))
