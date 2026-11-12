import java.util.*;

public class GraphAranas {
    private final Map<Character, List<Character>> adjacencyList =
            new TreeMap<>();

    // Add a vertex if it does not already exist.
    void addVertex(char vertex) {
        adjacencyList.putIfAbsent(vertex, new ArrayList<>());
    }

    // Add an undirected edge.
    void addEdge(char first, char second) {
        addVertex(first);
        addVertex(second);
        adjacencyList.get(first).add(second);
        adjacencyList.get(second).add(first);
    }

    // Sort neighbors so traversal follows alphabetical order.
    void sortNeighbors() {
        for (List<Character> neighbors : adjacencyList.values()) {
            Collections.sort(neighbors);
        }
    }

    // Breadth-First Search using a queue.
    void bfs(char start) {
        Set<Character> visited = new HashSet<>();
        Queue<Character> queue = new LinkedList<>();

        visited.add(start);
        queue.add(start);

        while (!queue.isEmpty()) {
            char current = queue.remove();
            System.out.print(current + " ");

            for (char neighbor : adjacencyList.get(current)) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.add(neighbor);
                }
            }
        }
    }

    // Depth-First Search using recursion.
    void dfs(char current, Set<Character> visited) {
        visited.add(current);
        System.out.print(current + " ");

        for (char neighbor : adjacencyList.get(current)) {
            if (!visited.contains(neighbor)) {
                dfs(neighbor, visited);
            }
        }
    }

    public static void main(String[] args) {
        GraphAranas graph = new GraphAranas();

        // Graph based on the unique letters A, R, N, S.
        // Edges: A-R, A-N, R-S, N-S.
        graph.addEdge('A', 'R');
        graph.addEdge('A', 'N');
        graph.addEdge('R', 'S');
        graph.addEdge('N', 'S');

        graph.sortNeighbors();

        System.out.print("Graph BFS: ");
        graph.bfs('A');

        System.out.print("\nGraph DFS: ");
        graph.dfs('A', new HashSet<>());

        System.out.println();
    }
}
