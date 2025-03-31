import networkx as nx

# Definir las conexiones entre nodos con pesos corregidos
grafo = {
    "Pantitlan": {"Jamaica": 5, "San Lazaro": 3, "Oceania": 7},
    "Jamaica": {"Santa Anita": 4, "Chabacano": 6, "Candelaria": 2, "Pantitlan": 5},
    "San Lazaro": {"Morelos": 3, "Candelaria": 8, "Oceania": 6, "Pantitlan": 3},
    "Oceania": {"San Lazaro": 6, "Consulado": 4, "Pantitlan": 7},
    "Santa Anita": {"Jamaica": 4, "Chabacano": 5, "Atlalilco": 3},
    "Chabacano": {"Santa Anita": 5, "Jamaica": 6, "Ermita": 7, "Pino Suarez": 4, "Salto del Agua": 5, "Centro Medico": 6},
    "Candelaria": {"San Lazaro": 8, "Morelos": 3, "Pino Suarez": 7, "Jamaica": 2},
    "Morelos": {"San Lazaro": 3, "Candelaria": 3, "Consulado": 4, "Garibaldi": 5},
    "Consulado": {"Martin Carrera": 6, "Morelos": 4, "Oceania": 4, "La Raza": 7},
    "Atlalilco": {"Santa Anita": 3, "Ermita": 4},
    "Ermita": {"Chabacano": 7, "Atlalilco": 4, "Zapata": 5},
    "Pino Suarez": {"Chabacano": 4, "Bellas Artes": 6, "Salto del Agua": 7, "Candelaria": 7},
    "Salto del Agua": {"Balderas": 5, "Bellas Artes": 6, "Pino Suarez": 7, "Chabacano": 5},
    "Centro Medico": {"Tacubaya": 8, "Chabacano": 6, "Zapata": 7, "Balderas": 4},
    "Garibaldi": {"Guerrero": 5, "Bellas Artes": 6, "Morelos": 5},
    "Martin Carrera": {"Consulado": 6, "18 de Marzo": 7, "La Villa": 8},
    "La Raza": {"18 de Marzo": 5, "Guerrero": 6, "Consulado": 7, "Instituto": 3},
    "Zapata": {"Mixcoac": 4, "Centro Medico": 7, "Ermita": 5, "CU": 6},
    "Bellas Artes": {"Hidalgo": 7, "Garibaldi": 6, "Salto del Agua": 6, "Pino Suarez": 6},
    "Balderas": {"Hidalgo": 5, "Tacubaya": 7, "Centro Medico": 4, "Salto del Agua": 5},
    "Tacubaya": {"Panteones": 6, "Mixcoac": 7, "Balderas": 7, "Centro Medico": 8},
    "Guerrero": {"La Raza": 6, "Hidalgo": 7, "Garibaldi": 5},
    "18 de Marzo": {"Instituto": 6, "La Raza": 5, "Martin Carrera": 7, "La Villa": 8},
    "Instituto": {"El Rosario": 9, "La Raza": 3, "18 de Marzo": 6},
    "Hidalgo": {"Panteones": 7, "Bellas Artes": 7, "Guerrero": 7, "Balderas": 5},
    "Panteones": {"Tacubaya": 6, "El Rosario": 8, "Hidalgo": 7},
    "La villa": {},
    "Mixcoac": {},
    "CU": {},
    "El Rosario": {}
}

# Crear el grafo
def crearGrafo(G):
    G = nx.Graph()
    for nodo, conexiones in grafo.items():
        for conexion, peso in conexiones.items():
            G.add_edge(nodo, conexion, weight=peso)
    return G

# Asignar valores fijos a los nodos
valores_nodos = {
    "Pantitlan": (3), "Jamaica": (5), "San Lazaro": (2), "Oceania": (4), "Santa Anita": (6),
    "Chabacano": (7), "Candelaria": (8), "Morelos": (5), "Consulado": (6), "Atlalilco": (3),
    "Ermita": (4), "Pino Suarez": (7), "Salto del Agua": (6), "Centro Medico": (9), "Garibaldi": (5),
    "Martin Carrera": (8), "La Raza": (6), "Zapata": (7), "Bellas Artes": (5), "Balderas": (9),
    "Tacubaya": (4), "Guerrero": (6), "18 de Marzo": (7), "Instituto": (5), "Hidalgo": (6), "Panteones": (8),
    "La Villa": (3), "Mixcoac": (4), "CU": (8), "El Rosario": (4)
}

def valoresNodos(G):
    nx.set_node_attributes(G, valores_nodos, "value")

# Imprimir los nodos, sus valores y conexiones con pesos
def printGrafo(G):
    valores_nodos = valoresNodos(G)
    for nodo in G.nodes():
        conexiones = [(vecino, G[nodo][vecino]['weight']) for vecino in G.neighbors(nodo)]
        print(f"{nodo} (Valores: {valores_nodos[nodo]}): {conexiones}")