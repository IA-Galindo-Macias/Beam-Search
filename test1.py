import networkx as nx
import matplotlib.pyplot as plt

from enum import IntEnum
from beam import beam_search, Graph


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

def plot_graph():
    """Construye una funcion para graficar patito feo :'("""

    # Etiquetas
    names = {
        Cities.TIJUANA: "Tijuana",
        Cities.TECATE: "Tecate",
        Cities.MEXICALI: "Mexicali",
        Cities.ROSARITO: "Rosarito",
        Cities.ENSENADA: "Ensenada",
        Cities.SAN_FELIPE: "San Felipe",
        Cities.SAN_QUINTIN: "San Quintin",
        Cities.GUERRERO_NEGRO: "Guerrero Negro"
    }

    # Posiciones de nodos
    positions = {
        Cities.TIJUANA: (0, 0),
        Cities.ROSARITO: (-0.5, -0.1),
        Cities.TECATE: (1.5, 0),
        Cities.ENSENADA: (-0.2, -0.3),
        Cities.MEXICALI: (3, 0),
        Cities.SAN_FELIPE: (3, -0.5),
        Cities.SAN_QUINTIN: (-0.2, -0.8),
        Cities.GUERRERO_NEGRO: (1.4, -1)
    }

    def draw_graph(graph, route):
        nx_graph = graph.as_networkx()
        route_edges = list(zip(route.path[:-1], route.path[1:]))
        edge_labels = {
            (origen, destino): weight
            for origen, destino in nx_graph.edges()
            for weight, neighbor in graph.neighbors(origen)
            if neighbor == destino
        }

        labels = {
            node: names[node]
            for node in positions.keys()
        }

        # Dibujar el grafo en esta iteracion
        plt.figure(figsize=(8, 8))
        nx.draw(
            nx_graph,
            pos=positions,
            with_labels=True,
            labels=labels,
            node_size=1000,
            node_color="lightblue",
            font_size=10,
            font_color="black"
        )

        nx.draw_networkx_nodes(
            graph,
            pos=positions,
            nodelist=route.path,
            node_color="red",
            node_size=1200
        )

        nx.draw_networkx_edges(
            graph.as_networkx(),
            pos=positions,
            edgelist=route_edges,
            edge_color="red",
            width=2
        )

        nx.draw_networkx_edge_labels(
            graph.as_networkx(),
            pos=positions,
            edge_labels=edge_labels,
            font_color="black"
        )

        plt.show()

    return draw_graph

solutions = beam_search(
    plot_func=plot_graph(),
    graph=baja_california,
    origin=Cities.TIJUANA,
    goal=Cities.ENSENADA,
    beam=4,
)

if solutions:
    print("-----")
    print("Ruta:", " -> ".join([city.name for city in solutions[0].path]))
    print("Distancia: ", solutions[0].distance, "km")
else:
    print("No hay solución")
