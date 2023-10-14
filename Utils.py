
from dataclasses import dataclass
from enum import IntEnum


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

    @dataclass
    class Node():
        key: int
        weight: float

        
    def __init__(self, nodes:int) -> None:
        assert nodes > 0
        
        self.nodes = nodes
        self._adj = [ [] for i in range(nodes) ]


    def add_directed_edge(self, p1:int, p2:int, weight=1):
        assert p1 < len(self._adj) and p1 >= 0
        assert p2 < len(self._adj) and p2 >= 0
        
        self._adj[p1].append( Graph.Node(p2, weight))
        return self
    
        
    def add_edge(self, p1:int, p2:int, weight=1):
        return self\
            .add_directed_edge(p1,p2,weight)\
            .add_directed_edge(p2,p1,weight)

    
    def get_vertices(self,p1:int) -> list:
        assert p1 < len(self._adj) and p1 >= 0
        return [ (node.weight ,node.key) for node in self._adj[p1] ]


    def get_weight(self, p1, p2) -> list:
        assert p1 < len(self._adj) and p1 >= 0
        return [
            node[0] for node in filter(
                lambda node: node[1] == p2,
                self.get_vertices(p1)
            )
        ]


baja_california = Graph(len(Cities))\
    .add_edge(Cities.TIJUANA, Cities.TECATE, 52)\
    .add_edge(Cities.TIJUANA, Cities.ROSARITO, 20)\
    .add_edge(Cities.ROSARITO, Cities.ENSENADA, 85)\
    .add_edge(Cities.TECATE, Cities.MEXICALI, 135)\
    .add_edge(Cities.TECATE, Cities.ENSENADA, 100)\
    .add_edge(Cities.MEXICALI, Cities.SAN_FELIPE, 197)\
    .add_edge(Cities.ENSENADA, Cities.SAN_FELIPE, 246)\
    .add_edge(Cities.ENSENADA, Cities.SAN_QUINTIN, 185)\
    .add_edge(Cities.SAN_FELswIPE, Cities.GUERRERO_NEGRO, 394)\
    .add_edge(Cities.SAN_QUINTIN, Cities.GUERRERO_NEGRO, 425)
