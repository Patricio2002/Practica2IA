import networkx as nx

# Definir los nodos con sus conexiones
nodos = {
  "Metropolis": (8.3, 153, 1927, ["Godzilla","El planeta de los simios"]),
  "Godzilla": (7.6, 96,1954, ["La naranja mecanica","Soylent Green"]),
  "El planeta de los simios": (8.0,112,1968,["Star Wars: Episodio IV","Alien"]),
  "La naranja mecanica": (8.2, 136, 1971,[]),
  "Soylent Green": (7.0,97,1973,["Blade Runner","Tron"]),
  "Star Wars: Episodio IV": (8.6, 121,1977,["Star Wars: Episodio V","Alien"]),
  "Alien": (8.5,117, 1979,["E.T.","Ghostbusters","The Terminator"]),
  "Star Wars: Episodio V": (8.7,124,1980,["Star Wars: Episodio VI","Volver al futuro"]),
  "E.T.": (7.9,115,1982,[]),
  "Blade Runner": (8.1,117,1982,[]),
  "Tron": (6.7,96,1982,[]),
  "Star Wars: Episodio VI": (8.3,131,1983,["Star Wars: Episodio I","The Matrix"]),
  "The Terminator": (8.1,107,1984,["Men in Black","Independence Day"]),
  "Ghostbusters": (7.8,105,1984,[]),
  "Volver al futuro": (8.5,116,1985,["Jurassic Park","Doce Monos"]),
  "Jurassic Park": (8.2,127,1993,[]),
  "Doce Monos": (8.0,129,1995,[]),
  "Independence Day": (7.0,145,1996,[]),
  "Men in Black": (7.3,98,1997,[]),
  "Star Wars: Episodio I": (6.5,136,1999,[]),
  "The Matrix": (8.7,136,1999,[])
}

# Crear el grafo
def crearGrafo():
  G = nx.DiGraph()
  for nodo, (imdb, duracion, anio, hijos) in nodos.items():
    G.add_node(nodo, imdb=imdb, duracion=duracion, anio=anio)
    for hijo in hijos:
        G.add_edge(nodo, hijo)
  return G

grafo=crearGrafo()

def heuristic(G, nodo):
  """Heurística basada en los valores de los nodos."""
  return (G.nodes[nodo]['anio']/100) + G.nodes[nodo]['imdb'] - abs(G.nodes[nodo]['duracion'] - 120)

# Implementación de Hill Climbing
def ascenso(G, inicio):
  actual = inicio
  while True:
    vecinos = list(G.successors(actual))
    if not vecinos:
        return actual
    mejor_vecino = max(vecinos, key=lambda n: heuristic(G, n))
    if heuristic(G, mejor_vecino) <= heuristic(G, actual):
        return actual
    actual = mejor_vecino

# Dibujar el grafo en la terminal
def dibujarGrafo(G):
    for nodo in G.nodes:
        hijos = list(G.successors(nodo))
        print(f"{nodo} -> {', '.join(hijos) if hijos else '∅'}")

# Ejecutar Hill Climbing desde el nodo 'A'
mejor_nodo = ascenso(grafo, "Metropolis")
print(f"El mejor nodo encontrado es: {mejor_nodo}")

# Dibujar el grafo en la terminal
dibujarGrafo(grafo)
