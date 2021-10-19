# 8. Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).

print('введите три числа: ')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a < b < c or a > b > c:
    print(f'среднее число {b}')
if b < a < c or b > a > c:
    print(f'среднее число {a}')
if b < c < a or b > c > a:
    print(f'среднее число {c}')
if a == b or a == c or b == c:
    print("среднего нет")
