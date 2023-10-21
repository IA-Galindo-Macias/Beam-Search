
import operator
from functools import reduce

from Utils import Graph, Route, log_output


def valid_route(route, origin, goal):
    """Verificar si una ruta es valida dentro del grafo"""    
    return goal in route.path and origin in route.path

def solutions(origin, goal, routes):
    """Lista de posibles soluciones"""
    return [
        route
        for route in routes
        if valid_route(route, origin, goal)
    ]

def solutions_found(origin, goal, routes):
    """Verificar si hay por lo menos 1 solucion"""
    return bool(solutions(origin, goal, routes))

def avalable_routes(graph,route):
    """Rutas disponibles con todos los nodos disponibles"""
    return [
        route.extend(city)
        for city in graph.neighbors(route.last())
        if not city[1] in route.path
    ]

@log_output
def extract_best(graph, routes, beam):
    return sorted(
        reduce(
            operator.add,
            [avalable_routes(graph,route) for route in routes]
        ),
        key=lambda route: route.distance
    )[:beam]

def beam_search(graph, origin, goal, beam):
    """Buscar una ruta con Beam Search"""

   
    def beam_search_route(routes):
        if not routes:
            # si el array rutas esta vacio
            return []

        return solutions(origin, goal, routes)\
            if solutions_found(origin, goal, routes) \
            else beam_search_route(
                extract_best(graph, routes, beam)
            ) 
    
    return beam_search_route([Route([origin], 0)])
