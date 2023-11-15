class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def get_vertices(self):
        return list(self.graph.keys())

    def add_edge(self, start, end, weight=None):
        if weight is None:
            weight = 1
        if start not in self.graph:
            self.add_vertex(start)
        if end not in self.graph:
            self.add_vertex(end)
        self.graph[start].append((end, weight))
        self.graph[end].append((start, weight))

    def get_edges(self):
        edges = []
        for vertex, neighbors in self.graph.items():
            for neighbor, weight in neighbors:
                edges.append((vertex, neighbor, weight))
        return edges

    def get_isolated_vertices(self):
        isolated_vertices = []
        for vertex in self.get_vertices():
            neighbor_vertices = set()
            for neighbors in self.graph[vertex]:
                neighbor_vertices.add(neighbors[0])

            # Self-Looping Case
            if len(neighbor_vertices) == 1 and neighbor_vertices == set(vertex):
                isolated_vertices.append(vertex)

            # No Neighbors Case
            elif not neighbor_vertices:
                isolated_vertices.append(vertex)
        return isolated_vertices

    def is_connected(self):
        vertex = next(iter(self.graph))
        dfs_traversal = self.dfs_traversal(vertex)
        # When DFS Trav and length of graph are equal, you know each vertex is
        # Connected and you have a perfect connected graph
        if len(dfs_traversal) == len(self.graph):
            return True
        return False

    def bfs_traversal(self, startVertex=None):
        if startVertex is None:
            startVertex = self.get_vertices()[0]

        visited = set()
        queue = [startVertex]
        visited.add(startVertex)
        result = []

        while len(queue) != 0:
            vertex = queue.pop(0)
            result.append(vertex)
            for neighbors in self.graph[vertex]:
                if neighbors[0] not in visited:
                    queue.append(neighbors[0])
                    visited.add(neighbors[0])

        return result

    def dfs_traversal(self, startVertex=None, result=None):
        # Initializes if Empty
        if startVertex is None:
            startVertex = self.get_vertices()[0]

        if result is None:
            result = []

        result.append(startVertex)
        neighbors = self.graph[startVertex]

        for neighbor in neighbors:
            if neighbor[0] not in result:
                result = self.dfs_traversal(neighbor[0], result)

        return result

    # def find_path(self, startVertex, endVertex, path=None):
    #     # Initializes with a value
    #     if path is None:
    #         path = []
    #
    #     path = path + [startVertex]
    #     # If it's a self looping path
    #     if startVertex == endVertex:
    #         return path
    #
    #     # If the path isn't accessible via graph
    #     if startVertex not in self.graph:
    #         return []
    #
    #     # Using DFS to find a path
    #     for vertex in self.graph[startVertex]:
    #         if vertex[0] not in path:
    #             extended_path = self.find_path(vertex[0], endVertex, path)
    #             if extended_path:
    #                 return extended_path
    #     return []
    #
    # def find_all_paths(self, start_vertex, end_vertex, path=None):
    #     if path is None:
    #         path = []
    #     path = path + [start_vertex]
    #     if start_vertex == end_vertex:
    #         return [path]
    #     if start_vertex not in self.graph:
    #         return []
    #     paths = []
    #     # Returns all paths instead of just the first one found
    #     for vertex in self.graph[start_vertex]:
    #         if vertex[0] not in path:
    #             extended_paths = self.find_all_paths(vertex[0], end_vertex, path)
    #             for p in extended_paths:
    #                 paths.append(p)
    #     return paths

    def __str__(self):
        result = ""
        for key, item in self.graph.items():
            result += f"{key} : {item}\n"
        return result
