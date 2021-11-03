
version_2 = """
import random
from collections import Counter
n = 1000
numbers = [random.randint(1, 10) for _ in range(n)]


def commom_el(list):
    return Counter(list).most_common(1)

commom_el(numbers)
# print(commom_el(numbers))
"""


from timeit import timeit

print(timeit(stmt=version_2, number=100), 'for n =')

# 0.009577899996656924 for n = 10
# 0.02512370000476949 for n = 100
# 0.06297699999413453 for n = 300
# 0.09142149999388494 for n = 500
# 0.18171659999643452 for n = 1000
