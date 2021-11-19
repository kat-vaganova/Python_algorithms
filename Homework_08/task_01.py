# 1. На улице встретились N друзей.
# Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

from functools import reduce  # берет итерируемый объект и сворачивает (складывает) все его значения в одно.


friends_count = int(input('Сколько встретилось друзей: '))


def handshake(n):
    graph = [[int(i > j) for i in range(n)] for j in range(n)]
    print(*graph, sep='\n')
    count = reduce(lambda acc, x: acc + sum(x), graph, 0)
    return count


result = handshake(friends_count)
print(f'Количество рукопожатий {result}')
