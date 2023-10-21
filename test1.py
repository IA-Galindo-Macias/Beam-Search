
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

solutions = beam_search(
    graph = baja_california,
    origin = Cities.TIJUANA,
    goal = Cities.SAN_FELIPE,
    beam = 3
)

print("----------")
print("Ruta:", " -> ".join([city.name for city in solutions[0].path]))
print("Distancia: ", solutions[0].distance, "km")
