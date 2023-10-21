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
