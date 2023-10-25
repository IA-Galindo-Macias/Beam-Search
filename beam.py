import operator
from functools import reduce

from Utils import Graph, Route, log_output


def valid_solution(route, origin, goal):
    """Verificar si una ruta es valida dentro del grafo"""
    return origin in route.path and goal in route.path


def solutions(origin, goal, routes):
    """Lista de posibles soluciones"""
    return [
        route
        for route in routes
        if valid_solution(route, origin, goal)
    ]


def solutions_found(origin, goal, routes):
    """Verificar si hay por lo menos 1 solucion"""
    return bool(solutions(origin, goal, routes))


def available_routes(graph, route):
    """Rutas disponibles con todos los nodos disponibles"""
    return [
        route.extend(city, distance)
        for distance, city in graph.neighbors(route.last())
        if not city in route.path
    ]


@log_output
def extended_routes(graph, routes):
    for route in routes:
        print(f"Mejor ruta actual: {', '.join([city.name for city in route.path])} | Distancia: {route.distance}")
        
    """ retorna una lista con rutas extendidas """
    return sorted(
        reduce(
            operator.add,
            [available_routes(graph, route) for route in routes]
        ),
        key=lambda route: route.distance
    )


def beam_search(graph, origin, goal, beam, plot_func=lambda x, y: None):
    """Buscar una ruta con Beam Search"""
    assert beam >= 0

    def beam_search_route(routes):

        for route in routes:
            plot_func(graph, route)

        if not routes:  # si el array rutas esta vacio
            return []

        # aplica beam search a las rutas extendidas
        return solutions(origin, goal, routes)\
            if solutions_found(origin, goal, routes)\
            else beam_search_route(
                # extrae los mejores 'beam' casos
                extended_routes(graph, routes)[:beam]
        )

    return beam_search_route([Route([origin], 0)])
