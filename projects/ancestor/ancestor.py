from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    # create graph of ancestors
    for x in ancestors:
        graph.add_vertex(x[0])
        graph.add_vertex(x[1])
        graph.add_edge(x[1], x[0])
    
    # graph.dft(starting_node)
    print(graph.vertices)
    
    if len(graph.vertices[starting_node]) == 0:
        return -1


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6),
                          (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 9)