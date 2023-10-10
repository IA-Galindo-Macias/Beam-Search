from enum import IntEnum
import heapq

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
    def validEdge(cls,p1,p2):
        if p1 == p2:
            raise Exception("No se puede unir una ciudad con si misma")

    @classmethod
    def setWeight(cls, p1, p2, weight):
        cls.validEdge(p1,p2)
        cls._adjMatrix[p1][p2] = weight
        cls._adjMatrix[p2][p1] = weight
        return cls

    @classmethod
    def getWeight(cls, p1, p2):
        cls.validEdge(p1,p2)
        return cls._adjMatrix[p1][p2]





Mapa = Graph(len(Cities))\
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
    

    

beam = 3


customers = []
heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))

while customers:
    print(heapq.heappop(customers))
