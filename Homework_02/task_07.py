# 7. Написать программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

import random

n = random.randint(1, 1000)

summa = 0
for i in range(1, n+1):
    summa += i
if summa == n * (n + 1)/2:
    print(True)
else:
    print(False)
