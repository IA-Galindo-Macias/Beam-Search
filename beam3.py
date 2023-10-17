
import operator
from functools import reduce

from Utils import Cities, Graph, Route


def valid_route(route, origin, goal):
    return goal in route.path and origin in route.path

def solutions_found(origin, goal, routes):
    return len(solutions(origin, goal, routes)) > 0

def solutions(origin, goal, routes):
    return [
        route
        for route in routes
        if valid_route(route, origin, goal)
    ]

def avalable_routes(graph,route):
    return [
        route.extend(city)
        for city in graph.get_vertices(route.last())
        if not city[1] in route.path
    ]

def beam_search(graph, origin, goal, beam):    
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

if __name__ == '__main__':

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
        graph= baja_california,
        origin= Cities.TIJUANA,
        goal= Cities.SAN_FELIPE,
        beam=7
    )
    
    print("Salida")
    for i in solutions[0].path:
        print(i.name)
