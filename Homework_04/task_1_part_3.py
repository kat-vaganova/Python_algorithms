
version_3 = """
import random
n = 1000
numbers = [random.randint(1, 5) for _ in range(n)]


def count_el(list, x):
    count = 0
    for el in list:
        if el == x:
            count += 1
    return count


x = max(numbers, key=numbers.count)


# print(x, 'встречается', count_el(numbers, x), 'раз')"""


from timeit import timeit

print(timeit(stmt=version_3, number=100), 'for n =')

# 0.0066829999996116385 for n = 10
# 0.0066829999996116385 for n = 100
# 0.24055990000488237 for n = 300
# 0.6282772999984445 for n = 500
# 2.273041899999953 for n = 1000
