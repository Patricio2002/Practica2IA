import random

estaciones = {
    1: ('Pantitlan', 3, 54), 2: ('Jamaica', 5, 31), 3: ('San Lazaro', 2, 55),
    4: ('Oceania', 4, 38), 5: ('Santa Anita', 6, 19), 6: ('Chabacano', 7, 19),
    7: ('Candelaria', 8, 49), 8: ('Morelos', 5, 27), 9: ('Consulado', 6, 35),
    10: ('Atlalilco', 3, 25), 11: ('Ermita', 4, 44), 12: ('Pino Suarez', 7, 34),
    13: ('Salto del Agua', 6, 32), 14: ('Centro Medico', 9, 42), 15: ('Garibaldi', 5, 20),
    16: ('Martin Carrera', 8, 51), 17: ('La Raza', 6, 60), 18: ('Zapata', 7, 58),
    19: ('Bellas Artes', 5, 43), 20: ('Balderas', 9, 43), 21: ('Tacubaya', 4, 16),
    22: ('Guerrero', 6, 32), 23: ('18 de Marzo', 7, 30), 24: ('Instituto', 5, 57),
    25: ('Hidalgo', 6, 47), 26: ('Panteones', 8, 34), 27: ('La Villa', 3, 27),
    28: ('Mixcoac', 4, 18), 29: ('CU', 8, 49), 30: ('El Rosario', 4, 35)
}

# Invertimos el diccionario para obtener claves por valor
estaciones_invertidas = {v: k for k, v in estaciones.items()}

largo = 10  # Longitud del material genético
num = 5  # Cantidad de individuos en la población
pressure = 2  # Número de individuos seleccionados para reproducción
mutation_chance = 0.5  # Probabilidad de mutación

def obtener_valor_unico(usados, min_val, max_val):
    """ Genera un índice aleatorio único que no esté en la lista de usados """
    nuevo_valor = random.randint(min_val, max_val)
    while nuevo_valor in usados:
        nuevo_valor = random.randint(min_val, max_val)
    usados.add(nuevo_valor)
    return nuevo_valor

def individual(min_val, max_val):
    """ Crea un individuo con valores aleatorios únicos """
    usados = set()
    return [estaciones[obtener_valor_unico(usados, min_val, max_val)] for _ in range(largo)]

def crear_poblacion():
    """ Crea una población de individuos """
    return [individual(1, 30) for _ in range(num)]

def calcular_fitness(ind):
    """ Calcula el fitness de un individuo """
    return sum(peso - tiempo for _, peso, tiempo in ind)

def seleccion_y_reproduccion(poblacion):
    """ Selecciona los mejores individuos y crea una nueva generación """
    puntuados = sorted(poblacion, key=calcular_fitness)
    seleccionados = puntuados[-pressure:]
    
    nueva_poblacion = seleccionados[:]
    for _ in range(len(poblacion) - pressure):
        padre1, padre2 = random.sample(seleccionados, 2)
        punto = random.randint(1, largo - 1)
        hijo = padre1[:punto] + padre2[punto:]
        nueva_poblacion.append(hijo)
    
    return nueva_poblacion

def mutacion(poblacion):
    """ Aplica mutaciones aleatorias a la población """
    for i in range(len(poblacion) - pressure):
        if random.random() <= mutation_chance:
            punto = random.randint(0, largo - 1)
            usados = {estaciones_invertidas[val] for val in poblacion[i]}
            nuevo_valor = obtener_valor_unico(usados, 1, 30)
            poblacion[i][punto] = estaciones[nuevo_valor]
    return poblacion

# Inicializar población
poblacion = crear_poblacion()
print("Población Inicial:")
for i, ind in enumerate(poblacion, 1):
    print(f"Individuo {i}: {ind}")

# Evolución
for _ in range(5000):
    poblacion = seleccion_y_reproduccion(poblacion)
    poblacion = mutacion(poblacion)

print("\nPoblación Final:")
for i, ind in enumerate(poblacion, 1):
    print(f"Individuo {i}: {ind}")