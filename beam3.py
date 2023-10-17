
import operator
from enum import IntEnum
from functools import reduce

from Utils import Graph, Route

# -----------------------------------------------------------------------------
# Métodos 
# -----------------------------------------------------------------------------

def valid_route(route, origin, goal):
    """Verificar si una ruta es valida dentro del grafo"""    
    return goal in route.path and origin in route.path

def solutions_found(origin, goal, routes):
    """Verificar si hay por lo menos 1 solucion"""
    return len(solutions(origin, goal, routes)) > 0

def solutions(origin, goal, routes):
    """Lista de posibles soluciones"""
    return [
        route
        for route in routes
        if valid_route(route, origin, goal)
    ]

def avalable_routes(graph,route):
    """Rutas disponibles con todos los nodos disponibles"""
    return [
        route.extend(city)
        for city in graph.neighbors(route.last())
        if not city[1] in route.path
    ]

def beam_search(graph, origin, goal, beam):
    """Buscar una ruta con Beam Search"""
    def beam_search_route(routes):
        if not routes:
            # si el array rutas esta vacio
            return []

        return solutions(origin, goal, routes)\
            if solutions_found(origin, goal, routes) \
            else beam_search_route(
                sorted(
                    reduce(
                        operator.add,
                        [avalable_routes(graph,route) for route in routes]
                    ),
                    key=lambda route: route.distance
                )[:beam]
            ) 
    
    return beam_search_route([Route([origin], 0)])

# -----------------------------------------------------------------------------
# Ejemplos de aplicacion 
# -----------------------------------------------------------------------------


def test2():
    """ 
    Ejemplo del video:
    - https://youtu.be/jhoXO1XF6Fk?si=rmkGtnaS0533N1P0
    """
    
    class Node(IntEnum):
        A = 0
        B = 1
        C = 2
        D = 3
        E = 4
        F = 5
        G = 6
        H = 7

    video = Graph(len(Node))\
        .add_edge(Node.A, Node.B, 11)\
        .add_edge(Node.A, Node.C, 14)\
        .add_edge(Node.A, Node.D, 7)\
        .add_edge(Node.B, Node.E, 15)\
        .add_edge(Node.C, Node.D, 18)\
        .add_edge(Node.C, Node.E, 8)\
        .add_edge(Node.C, Node.F, 10)\
        .add_edge(Node.D, Node.F, 25)\
        .add_edge(Node.C, Node.F, 10)\
        .add_edge(Node.E, Node.H, 9)\
        .add_edge(Node.F, Node.G, 20)\
        .add_edge(Node.G, Node.H, 10)
        
    solutions = beam_search(
        graph= video,
        origin= Node.A,
        goal= Node.G,
        beam=3
    )

    print("Ruta:", " -> ".join([city.name for city in solutions[0].path]))
    print("Distancia: ", solutions[0].distance)
    

def test1():

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
        beam = 7
    )

    print("Ruta:", " -> ".join([city.name for city in solutions[0].path]))
    print("Distancia: ", solutions[0].distance, "km")
    
if __name__ == '__main__':
    test1()
