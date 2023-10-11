
from beam import Cities
from beam import Graph

origin = Cities.TIJUANA
goal = Cities.GUERRERO_NEGRO
    
baja_california = Graph(len(Cities))\
    .setWeight(Cities.TIJUANA, Cities.TECATE, 52)\
    .setWeight(Cities.TIJUANA, Cities.ROSARITO, 20)\
    .setWeight(Cities.ROSARITO, Cities.ENSENADA, 85)\
    .setWeight(Cities.TECATE, Cities.MEXICALI, 135)\
    .setWeight(Cities.TECATE, Cities.ENSENADA, 100)\
    .setWeight(Cities.MEXICALI, Cities.SAN_FELIPE, 197)\
    .setWeight(Cities.ENSENADA, Cities.SAN_FELIPE, 246)\
    .setWeight(Cities.ENSENADA, Cities.SAN_QUINTIN, 185)\
    .setWeight(Cities.SAN_FELIPE, Cities.GUERRERO_NEGRO, 394)\
    .setWeight(Cities.SAN_QUINTIN, Cities.GUERRERO_NEGRO, 425)

def route_distance(route):
    if len(route) == 0 or len(route) == 1:
        return 0

    sum = Graph.getWeight(route[0], route[1])
    for i in range(1,len(route)-1):
        sum += Graph.getWeight(route[i], route[i+1])

    return sum


def search_routes(route, origin, goal):
    if goal in route:           # ruta completada
        return route

    routes = []
    for index, distance in enumerate(Graph.getNodeAdj(route[-1])):
        if distance != 0 and not index in route:
            routes.append(route + [Cities(index)])

    return routes


def completed_route(route, goal):
    return goal in route


def beam_search(origin, goal):
    solution_not_found = True
    routes = [[origin]]         # ruta inicial
    
    while(solution_not_found):
        new_routes = []
        for route in routes:
            new_routes += search_routes(route, origin, goal)

        new_routes.sort(key=route_distance)
        routes = new_routes[:3]

        for route in routes:
            if completed_route(route, goal):
                return route

        
