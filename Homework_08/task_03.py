# 3. Написать программу,
# которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.


import random


# создание списка смежности невзвешенного графа.
def graph_create(n):
    return {i: {j for j in range(random.randint(1, n), random.randint(2, n + 1)) if j != i} for i in range(1, n + 1)}


# обход в глубину.
def dfs(graph, vertex, visited):

    visited.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


num = random.randint(5, 15)  # глубина графа

g = graph_create(num)

# Подсчет количества связанных вершин.

visited = set()
num_el = 0
for v in g:
    if v not in visited:
        dfs(g, v, visited)
        num_el += 1


print(*g.items(), sep='\n')
print(f'Количество связанных вершин: {num_el}')
print(visited)