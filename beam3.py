
import operator
from dataclasses import dataclass
from functools import reduce

from Utils import Cities, Graph


@dataclass
class Route():
    path: list
    distance: int

    def last(self):
        return self.path[-1]

    def extend(self, city: tuple):
        return Route(self.path + [city[1]], self.distance + city[0])


def avalable_routes(route):
    return [
        route.extend(city)
        for city in baja_california.get_vertices(route.last())
        if not city[1] in route.path
    ]


def valid_route(origin, goal, route):
    return goal in route.path and origin in route.path


def solution_finded(origin, goal, routes):
    return [
        route
        for route in routes
        if valid_route(origin, goal, route)
    ]


def beam_search(origin, goal, beam, routes):

    if not routes:              # si el array rutas esta vacio
        return []

    # 'var' as in 'let'
    solutions = solution_finded(origin, goal, routes)

    return solutions[0]\
        if len(solutions) > 0\
        else beam_search(
            origin,
            goal,
            beam,
            sorted(
                reduce(
                    operator.add,
                    [avalable_routes(route) for route in routes]
                ),
                key=lambda route: route.distance
            )[:beam]
    )


def beam_search_route(origin, goal, beam):
    return beam_search(origin, goal, beam, [Route([origin], 0)])


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


origin = Cities.GUERRERO_NEGRO
goal = Cities.TECATE
beam = 7


print("Salida <<<")
for i in beam_search_route(origin, goal, beam).path:
    print(i.name)
