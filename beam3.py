
import operator
from functools import reduce
import networkx as nx
import matplotlib.pyplot as plt

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

def available_routes(graph,route):
    """Rutas disponibles con todos los nodos disponibles"""
    return [
        route.extend(city)
        for city in graph.neighbors(route.last())
        if not city[1] in route.path
    ]

@log_output
def extract_best(graph, routes):
    return sorted(
        reduce(
            operator.add,
            [available_routes(graph,route) for route in routes]
        ),
        key=lambda route: route.distance
    )

def beam_search(graph, origin, goal, beam, positions, city_names):
    """Buscar una ruta con Beam Search"""

   
    def beam_search_route(routes):
        if not routes:
            # si el array rutas esta vacio
            return []
        
        plot_graph(graph, routes, positions, city_names)

        return solutions(origin, goal, routes)\
            if solutions_found(origin, goal, routes)\
            else beam_search_route(
                extract_best(graph, routes)[:beam]
            ) 
    
    return beam_search_route([Route([origin], 0)])

def plot_graph(graph, routes, positions, city_names):
    for route in routes:
        current_route_edges = [(route.path[i], route.path[i + 1]) for i in range(len(route.path) - 1)]
        labels = {node: city_names[node] for node in positions.keys()}

        # Diccionario de etiquetas de aristas
        edge_labels = {}
        for u, v in graph.as_networkx().edges():
            for weight, neighbor in graph.neighbors(u):
                if neighbor == v:
                    edge_labels[(u, v)] = weight

            
        # Dibujar el grafo en esta iteracion
        plt.figure(figsize=(8, 8))
        #pos = nx.spring_layout(graph.as_dict())
        nx.draw(
            graph.as_networkx(), 
            pos=positions, 
            with_labels=True, 
            labels=labels, 
            node_size=1000, 
            node_color="lightblue", 
            font_size=10, 
            font_color="black"
        )
        nx.draw_networkx_nodes(graph, pos=positions, nodelist=route.path, node_color="red", node_size=1200)
        nx.draw_networkx_edge_labels(graph.as_networkx(), pos=positions, edge_labels=edge_labels, font_color="black")
        nx.draw_networkx_edges(graph.as_networkx(), pos=positions, edgelist=current_route_edges, edge_color="red", width=2)
        plt.title(f"Beam Search - Iteración {route.distance}km: {', '.join([city.name for city in route.path])}")
        plt.show()