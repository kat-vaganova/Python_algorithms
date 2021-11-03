# решето Эратосфена

n = 10000000000000000

def eratosthenes(n):
    sieve = list(range(n+1))
    sieve[1] = 0  # 1 не является простым числом
    for i in sieve:
        if i > 0:
            for j in range(i+i, len(sieve), i):
                sieve[j] = 0
    return sieve


# print(*[i for i in eratosthenes(n) if i != 0])

from timeit import timeit
print(timeit(number=100), 'for n =')

# 5.599998985417187e-06 for n = 100
# 5.599998985417187e-06 for n = 1000
# 5.599998985417187e-06 for n = 10000
# 5.800000508315861e-06 for n = 100000
# 5.49999822396785e-06 for n = 1000000
# 5.699999746866524e-06 for n = 10000000000000000
