"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque

class Graph:

    """Represent a graph as a dictionary of vertices
        mapping labels to edges.
    """

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        queue.enqueue(starting_vertex)
        result = []
        visited = {}
        visited[starting_vertex] = True

        while queue.size():
            current_vertex = queue.dequeue()
            result.append(current_vertex)

            for neighbor in self.vertices[current_vertex]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    queue.enqueue(neighbor)
        for vertex in result:
            print(vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = [starting_vertex]
        result = []
        visited = {}

        visited[starting_vertex] = True
        while len(stack):
            current_vertex = stack.pop()
            result.append(current_vertex)

            for neighbor in self.vertices[current_vertex]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    stack.append(neighbor)

        for vertex in result:
            print(vertex)
        
        return result

    def _dfs_helper(self, v, path=[]):
        path += [v]
        for neighbor in self.vertices[v]:
            if neighbor not in path:
                path = self._dfs_helper(neighbor, path)
        return path

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = [False] * (len(self.vertices))
        result = self._dfs_helper(starting_vertex)     
        for v in result:
            print(v)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])
        visitied = set()
       
        if starting_vertex == destination_vertex:
            return [starting_vertex, destination_vertex]
        
        while queue.size() > 0:
            visitied = set()
            path = queue.dequeue()
            vertex = path[-1]
            if vertex not in visitied:
                if vertex == destination_vertex:
                    return path
                
                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    np = list(path)
                    np.append(neighbor)
                    queue.enqueue(np)

                    if neighbor == destination_vertex:
                        return np
                
                visitied.add(vertex)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        stack = Stack()
        stack.push([starting_vertex])

        if starting_vertex == destination_vertex:
            return [starting_vertex, destination_vertex]
        
        while stack.size():
            path = stack.pop()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                
                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    np = list(path)
                    np.append(neighbor)
                    stack.push(np)

                    if neighbor == destination_vertex:
                        return np
                
                visited.add(vertex)

    def dfs_recursive(self, starting_vertex, destination_vertex, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if path is None:
            path = [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors - set(path):
            findPath = self.dfs_recursive(neighbor, destination_vertex, path + [neighbor])
            if findPath is not None:
                return findPath


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    print(graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
