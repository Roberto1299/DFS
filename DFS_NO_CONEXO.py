from collections import defaultdict

def dfs(graph, node, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, component)

def find_connected_components(edges):
    graph = defaultdict(list)

    # Construir el grafo a partir de las aristas
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])


    # Imprimir la lista de adyacencia
    for node, neighbors in graph.items():
        print(f"Nodo {node}: {neighbors}")

    # Inicializar variables
    visited = {node: False for node in graph}
    components = []

    # Encontrar componentes conectados
    for node in graph:
        if not visited[node]:
            component = []
            dfs(graph, node, visited, component)
            components.append(component)

    return components

# Lista de nodos
nodes = list(range(50))

# Lista de aristas
edges = [
 (0, 29), (0, 46), (0, 21), (0, 14), (0, 38), (0, 31), (1, 41), (1, 31), (1, 21),
 (1, 17), (2, 9),  (2, 26), (2, 5),  (2, 25), (2, 4),  (3, 18), (3, 30), (3, 47),
 (4, 28), (4, 9),  (4, 8),  (5, 44), (5, 12), (6, 37), (6, 10), (7, 23), (7, 22),
 (7, 39), (9, 19), (9, 28), (9, 27), (11, 33),(13, 25),(13, 38),(13, 29),(14, 26),
 (14, 28),(14, 39),(15, 22),(15, 31),(15, 19),(15, 41),(16, 46),(16, 26),(16, 38),
 (16, 27),(17, 40),(17, 29),(18, 45),(18, 42),(18, 35),(18, 33),(18, 47),(20, 36),
 (20, 49),(20, 42),(22, 26),(22, 34),(23, 31),(23, 32),(23, 40),(24, 31),(24, 44),
 (25, 38), (26, 31), (27, 32), (29, 48), (29, 41), (30, 47), (30, 37), (33, 36),
 (33, 49), (34, 48), (35, 45), (36, 45), (37, 49), (37, 45), (37, 47), (38, 41),
 (40, 48), (41, 44), (42, 49), (43, 48), (45, 47)]

# Encontrar subgrafos no conexos
connected_components = find_connected_components(edges)

# Imprimir los nodos en cada subgrafo no conexo
for i, component in enumerate(connected_components):
    print(f"Subgrafo {i + 1}: {component}")