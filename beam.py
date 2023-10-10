from enum import IntEnum
import heapq

# -----------------------------------------------------------------------------

class Cities(IntEnum):
    # Nodos de BCgraph
    TIJUANA = 0 
    TECATE = 1
    MEXICALI = 2
    ROSARITO = 3
    ENSENADA = 4
    SAN_FELIPE = 5
    SAN_QUINTIN = 6
    GUERRERO_NEGRO = 7

class Graph():
    # instancia
    _instance = None
        
    # matriz de adyacencia
    _adjMatrix = []
        

    def __new__(cls, nodes=0):
        # hacerlo un singleton y crear la matriz de adyacencia
        if cls._instance is None:
            cls._instance = super(Graph, cls).__new__(cls)
            cls._adjMatrix = [[0] * nodes for i in range(nodes)]
            
        return cls._instance

    @classmethod
    def setWeight(cls, p1, p2, weight):
        cls._adjMatrix[p1][p2] = weight
        cls._adjMatrix[p2][p1] = weight
        return cls

    @classmethod
    def getWeight(cls, p1, p2):
        return cls._adjMatrix[p1][p2]

    @classmethod
    def getNodeAdj(cls, p1):
        return cls._adjMatrix[p1]
    
# -----------------------------------------------------------------------------


def distance(route):
    # distancia total de la ruta

    sum = 0
    for i in range(len(route) - 1):
        sum += Graph.getWeight(route[i], route[i+1])
    
    return sum


def search_routes(rute):
    cities_heap = []
    routes = []

    # desde el ultimo nodo agregado
    last_city = rute[-1]
    
    if last_city == goal:       # ya se llego al objetivo
        return rute
    
    for i,v in enumerate(Graph.getNodeAdj(last_city)):
        # si es adyacente y no se a pasado por la ciudad
        if v != 0 and not i in rute:
            # ordenarlos por distancia
            heapq.heappush(cities_heap, (v,Cities(i)))

    while cities_heap:
        _, city = heapq.heappop(cities_heap)
        routes.append( rute + [city] ) # crea una nueva lista

    # ciudades mas cercanas por las que no se ha pasado
    return routes






# grafo 
Graph(len(Cities))\
    .setWeight(Cities.TIJUANA, Cities.TECATE, 52)\
    .setWeight(Cities.TIJUANA, Cities.ROSARITO, 20)\
    .setWeight(Cities.ROSARITO, Cities.ENSENADA, 85)\
    .setWeight(Cities.TECATE, Cities.MEXICALI, 135)\
    .setWeight(Cities.TECATE, Cities.ENSENADA, 100)\
    .setWeight(Cities.MEXICALI, Cities.SAN_FELIPE, 197)\
    .setWeight(Cities.ENSENADA, Cities.SAN_FELIPE,246)\
    .setWeight(Cities.ENSENADA, Cities.SAN_QUINTIN,185)\
    .setWeight(Cities.SAN_FELIPE, Cities.GUERRERO_NEGRO, 394)\
    .setWeight(Cities.SAN_QUINTIN, Cities.GUERRERO_NEGRO,425)

# Ciudad
origin = Cities.TIJUANA
goal = Cities.GUERRERO_NEGRO

# tamaño
beam = 3

# Rutas
routes = [
    [origin],
]






new_routes = []
print("")
for route in routes:
    print(route)
    new_routes += search_routes(route)

new_routes.sort(key=distance)
routes = new_routes[:3]


new_routes.clear()
