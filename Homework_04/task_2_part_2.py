
n = 100000
d = None
c = True
for a in range(2, n):
    for b in range(1, n):
        if a != b and b != 1:
            if not a % b:
                c = False
                break
    if c == True:
        a = d
        # print(a, end=" ")
    c = True

from timeit import timeit
print(timeit(number=100), 'for n =')


# 5.599998985417187e-06 for n = 100
# 5.699999746866524e-06 for n = 1000
# 5.900001269765198e-06 for n = 10000
# процесс остановлен при n = 100000
