import heapq
from p21 import grafo, valoresNodos, crearGrafo, valores_nodos

def heuristic(a, b, node_values):
    """Heurística basada en los valores de los nodos."""
    return abs(node_values[a] - node_values[b])

def a_star(graph, start, goal, node_values):
    """Implementación del algoritmo A* para encontrar el camino más corto en un grafo."""
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph.nodes}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph.nodes}
    f_score[start] = heuristic(start, goal, node_values)
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Devuelve el camino en orden correcto
        
        for neighbor in graph.neighbors(current):
            cost = graph[current][neighbor]['weight']
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal, node_values)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None  # No hay camino posible


G=grafo
G=crearGrafo(G)
valoresNodos(G)
v=valores_nodos


start = "Pantitlan"
goal1 = "El Rosario"
goal2 = "CU"
goal3 = "Mixcoac"
goal4 = "La Villa"

path = a_star(G, start,goal1, v)
print("Camino encontrado de Pantitlan a El Rosario:", path)
path = a_star(G, start,goal2, v)
print("Camino encontrado de Pantitlan a CU:", path)
path = a_star(G, start,goal3, v)
print("Camino encontrado: de Pantitlan a Mixcoac:", path)
path = a_star(G, start,goal4, v)
print("Camino encontrado de Pantitlan a La Villa:", path)