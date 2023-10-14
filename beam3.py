
from dataclasses import dataclass

from Utils import Cities
from Utils import Graph

@dataclass
class Route():
    path: list
    distance: int

    def last(self):
        return self.path[-1]

    def extend(self, city:tuple):
        return Route( self.path + [city[1]], self.distance + city[0]) 

    
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


origin = Cities.TIJUANA
goal = Cities.GUERRERO_NEGRO
beam = 3


routes = [Route([origin], 0)]

new_routes = []
for route in routes:
    new_routes += [
        route.extend(city)
        for city in baja_california.get_vertices(route.last())
        if not city[1] in route.path
    ]

routes = sorted(new_routes, key=lambda x: x.distance)[:beam]

if len(list(filter(lambda x: goal in x.path, routes))) > 0:
    print("\nsolucion encontrada!\n")

new_routes.clear()

print(" ")
for i in routes: print(i);

# adj.sort()
    

# route = adj[:3]
