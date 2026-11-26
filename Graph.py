
class GraphRayven:

    def __init__(self):
        self.adjacency_list = {}

    # Add a vertex if it does not already exist.
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    # Add an undirected edge.
    def add_edge(self, first, second):
        self.add_vertex(first)
        self.add_vertex(second)

        self.adjacency_list[first].append(second)
        self.adjacency_list[second].append(first)

    # Sort neighbors alphabetically.
    def sort_neighbors(self):
        for neighbors in self.adjacency_list.values():
            neighbors.sort()

    # Breadth-First Search using a queue.
    def bfs(self, start):
        visited = set()
        queue = [start]

        visited.add(start)

        while queue:
            current = queue.pop(0)
            print(current, end=" ")

            for neighbor in self.adjacency_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    # Depth-First Search using recursion.
    def dfs(self, current, visited):
        visited.add(current)
        print(current, end=" ")

        for neighbor in self.adjacency_list[current]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


# Main Program
if __name__ == "__main__":

    graph = GraphRayven()

    # Graph based on RAYVEN.
    #
    # Edges:
    # R-A, R-V, A-Y, A-E, Y-N, V-N
    #
    # Add edges
    graph.add_edge('R', 'A')
    graph.add_edge('R', 'V')
    graph.add_edge('A', 'Y')
    graph.add_edge('A', 'E')
    graph.add_edge('Y', 'N')
    graph.add_edge('V', 'N')

    # Sort neighbors alphabetically.
    graph.sort_neighbors()

    # Display BFS
    print("Graph BFS: ", end="")
    graph.bfs('A')

    # Display DFS
    print("\nGraph DFS: ", end="")
    graph.dfs('A', set())

    print()
