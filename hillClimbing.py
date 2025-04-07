import networkx as nx
from collections import deque

# Crear el grafo
def crearGrafo():
  G = nx.DiGraph()
  for nodo, (imdb, duracion, anio, hijos) in nodos.items():
    G.add_node(nodo, imdb=imdb, duracion=duracion, anio=anio)
    for hijo in hijos:
        G.add_edge(nodo, hijo)
  return G

#Definicion de la Heuristica
def heuristic(G, nodo):
  """Heurística basada en los valores de los nodos."""
  return (G.nodes[nodo]['anio']/100) + G.nodes[nodo]['imdb'] - abs(G.nodes[nodo]['duracion'] - 120)

# Implementación de Hill Climbing
def ascenso(G, inicio, sol):
  actual=inicio
  recorrido = deque()
  orden = deque()
  orden.append (actual)
  while True:
    recorrido.append(actual)
    mejor = []
    aux = {}
    vecinos = list(G.successors(actual))
    if actual == sol:
      return recorrido
    if not vecinos:
      if not orden:
          return recorrido
      else:
          while orden:  # verifica si orden no está vacío
              actual = orden.popleft()
              if actual not in recorrido:
                  break
          else:
              return recorrido
    else:
      for i in vecinos:
        mejor.append(heuristic(G,i))
        aux[heuristic(G,i)] = i
      mejor.sort(reverse=True)
      for i in mejor:
        orden.append(aux[i])
      actual=aux[mejor[0]]

# Dibujar el grafo en la terminal
def dibujarGrafo(G):
    for nodo in G.nodes:
        hijos = list(G.successors(nodo))
        print(f"{nodo} -> {', '.join(hijos) if hijos else '∅'}")

# Definir los nodos con sus conexiones
nodos = {
  "Metropolis": (8.3, 153, 1927, ["Godzilla","El planeta de los simios"]),
  "Godzilla": (7.6, 96,1954, ["La naranja mecanica","Soylent Green"]),
  "El planeta de los simios": (8.0,112,1968,["Star Wars: Episodio IV","Alien"]),
  "La naranja mecanica": (8.2, 136, 1971,[]),
  "Soylent Green": (7.0,97,1973,["Blade Runner","Tron"]),
  "Star Wars: Episodio IV": (8.6, 121,1977,["Star Wars: Episodio V","The Terminator"]),
  "Alien": (8.5,117, 1979,["E.T.","Ghostbusters"]),
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

grafo=crearGrafo()
sol = "Jurassic Park" #Nodo objetivo
# Ejecutar Hill Climbing desde el nodo 'Metropolis'
recorrido = ascenso(grafo, "Metropolis",sol)
if recorrido[-1] == sol:
  for i in recorrido:
    print(f"{i}")
else:
  print("No llego a la solucion")

# Dibujar el grafo en la terminal
#dibujarGrafo(grafo)
