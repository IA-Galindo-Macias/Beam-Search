
from dataclasses import dataclass
from enum import IntEnum

def log_output(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)

        print("----------")
        for i, arg in enumerate(resultado):
            print(arg)
        
        return resultado
    return wrapper


@dataclass
class Route():
    path: list
    distance: int

    def last(self):
        return self.path[-1]

    def extend(self, city: tuple):
        return Route(self.path + [city[1]], self.distance + city[0])

    def __str__(self):
         return str(self.distance) \
             + "km: " \
             + " ".join([city.name for city in self.path]) 

    
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

    
    def neighbors(self,p1:int) -> list:
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
