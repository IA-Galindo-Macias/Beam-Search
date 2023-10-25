import networkx as nx
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


from enum import IntEnum
from beam import beam_search, Graph

# lista de ciudades en baja california
# ---------------------------------------------------------------------
class Cities(IntEnum):
    TIJUANA = 0
    TECATE = 1
    MEXICALI = 2
    ROSARITO = 3
    ENSENADA = 4
    SAN_FELIPE = 5
    SAN_QUINTIN = 6
    GUERRERO_NEGRO = 7

# Posiciones de nodos para networkX
# ---------------------------------------------------------------------
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

# grafo de baja california
# ---------------------------------------------------------------------
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

# networkX
# ---------------------------------------------------------------------
def plot_graph(cities_enum, positions):
    """Construye una funcion para graficar patito feo :'("""

    # Etiquetas
    names = {
        city.value: city.name
        for city in cities_enum
    }

    labels = {
        node: names[node]
        for node in names
    }

    def draw_graph(graph, route):
        # convertir grafo a DiGraph
        nx_graph = nx.DiGraph()
        for node in range(len(graph._adj)):
            for edge in graph._adj[node]:
                nx_graph.add_edge(node, edge.key, weight=edge.weight)

        # unir vertices
        route_edges = list(zip(route.path[:-1], route.path[1:]))

        # labels de pesos
        edge_labels = {
            (origen, destino): weight
            for origen, destino in nx_graph.edges()
            for weight, neighbor in graph.neighbors(origen)
            if neighbor == destino
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
            nx_graph,
            pos=positions,
            edgelist=route_edges,
            edge_color="red",
            width=2
        )

        nx.draw_networkx_edge_labels(
            nx_graph,
            pos=positions,
            edge_labels=edge_labels,
            font_color="black"
        )

        plt.show()

    return draw_graph

# Beam Search
# ---------------------------------------------------------------------
solutions = beam_search(
    # parametros de beam search
    graph=baja_california,
    origin=Cities.TIJUANA,
    goal=Cities.GUERRERO_NEGRO,
    beam=3,

    # funcion para graficar
    plot_func=plot_graph(Cities, positions)
)

# Salida del beam search
# ---------------------------------------------------------------------
if solutions:
    print("\n\n----- Mejor Ruta -----")
    print(solutions[0])
else:
    print("No hay solución")
