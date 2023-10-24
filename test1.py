from enum import IntEnum
from beam3 import beam_search, Graph

class Cities(IntEnum):
    TIJUANA = 0
    TECATE = 1
    MEXICALI = 2
    ROSARITO = 3
    ENSENADA = 4
    SAN_FELIPE = 5
    SAN_QUINTIN = 6
    GUERRERO_NEGRO = 7
        
baja_california = Graph(len(Cities))\
    .add_edge(Cities.TIJUANA, Cities.TECATE, 52)\
    .add_edge(Cities.TIJUANA, Cities.ROSARITO, 20)\
    .add_edge(Cities.ROSARITO, Cities.ENSENADA, 85)\
    .add_edge(Cities.TECATE, Cities.MEXICALI, 135)\
    .add_edge(Cities.TECATE, Cities.ENSENADA, 100)\
    .add_edge(Cities.MEXICALI, Cities.SAN_FELIPE, 197)\
    .add_edge(Cities.ENSENADA, Cities.SAN_FELIPE, 246)\
    .add_edge(Cities.ENSENADA, Cities.SAN_QUINTIN, 185)\
    .add_edge(Cities.SAN_FELIPE, Cities.GUERRERO_NEGRO, 394)\
    .add_edge(Cities.SAN_QUINTIN, Cities.GUERRERO_NEGRO, 425)

"""Networkx"""
# Etiquetas
city_names = {
    Cities.TIJUANA: "Tijuana",
    Cities.TECATE: "Tecate",
    Cities.MEXICALI: "Mexicali",
    Cities.ROSARITO: "Rosarito",
    Cities.ENSENADA: "Ensenada",
    Cities.SAN_FELIPE: "San Felipe",
    Cities.SAN_QUINTIN: "San Quintin",
    Cities.GUERRERO_NEGRO: "Guerrero Negro"
}

# Posiciones de nodos
posiciones_fijas = {
    Cities.TIJUANA: (0, 0),
    Cities.ROSARITO: (-0.5, -0.1),
    Cities.TECATE: (1.5, 0),
    Cities.ENSENADA: (-0.2, -0.3),
    Cities.MEXICALI: (3, 0),
    Cities.SAN_FELIPE: (3, -0.5),
    Cities.SAN_QUINTIN: (-0.2, -0.8),
    Cities.GUERRERO_NEGRO: (1.4, -1)
}

solutions = beam_search(
    graph = baja_california,
    origin = Cities.TIJUANA,
    goal = Cities.SAN_FELIPE,
    beam = 3,
    
    positions = posiciones_fijas,
    city_names = city_names
)

if solutions:
    print("-----")
    print("Ruta:", " -> ".join([city.name for city in solutions[0].path]))
    print("Distancia: ", solutions[0].distance, "km")
else:
    print("No hay solución")
