from util import Queue, Stack
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # 1. Build the graph
    # instantiate a new graph object
    graph = Graph()
    # loop over all pairs in ancestors
    for pair in ancestors:
        # add pair[0] and pair[1] to the graph
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # build the edges in reverse
        graph.add_edge(pair[1], pair[0])
    # Do a BFS (with paths)
    # create a queue
    q = Queue()
    # enqueue starting node inside a list
    q.enqueue([starting_node])
    # set a max path length to 1
    max_path_length = 1
    # set initial earlyest ancestor
    earliest_ancestor = -1
    # while queue has contents
    while q.size() > 0:
        # dequeue the path
        path = q.dequeue()
        # get the last vert
        vert = path[-1]
        # if path is longer or equal and the value is smaller, or if the path is longer
        if (len(path) >= max_path_length and vert < earliest_ancestor) or (len(path) > max_path_length):
            # set the earliest ancestor to the vert
            earliest_ancestor = vert
            # set the max path length to the len of the path
            max_path_length = len(path)
        # loop over each neighbor in the graphs vertices at index of vert
        for neighbor in graph.vertices[vert]:
            # make a copy of the path
            path_copy = list(path)
            # append neighbor to the coppied path
            path_copy.append(neighbor)
            # then enqueue the copied path
            q.enqueue(path_copy)
    # return earliest ancestor
    return earliest_ancestor