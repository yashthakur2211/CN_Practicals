class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def print_solution(self, dist):
        print("Vertex \t Distance from Source")
        for i in range(self.vertices):
            print(f"{i}\t\t{dist[i]}")

    def bellman_ford(self, src):
        dist = [float("inf")] * self.vertices
        dist[src] = 0

        for _ in range(self.vertices - 1):
            for u, v, w in self.graph:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        self.print_solution(dist)


# Example usage:
g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 2)
g.add_edge(2, 1, 3)
g.add_edge(1, 3, 6)
g.add_edge(2, 3, 1)
g.add_edge(2, 4, 4)
g.add_edge(3, 4, 2)

g.bellman_ford(0)
