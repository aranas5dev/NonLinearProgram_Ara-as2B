import java.util.*;

public class BinaryTreeAranas {
    static class Node {
        char data;
        Node left, right;

        Node(char data) {
            this.data = data;
        }
    }

    // Breadth-First Search: visit nodes level by level.
    static void bfs(Node root) {
        if (root == null) return;

        Queue<Node> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            Node current = queue.remove();
            System.out.print(current.data + " ");

            if (current.left != null) queue.add(current.left);
            if (current.right != null) queue.add(current.right);
        }
    }

    // Depth-First Search using Preorder: Root, Left, Right.
    static void dfsPreorder(Node node) {
        if (node == null) return;

        System.out.print(node.data + " ");
        dfsPreorder(node.left);
        dfsPreorder(node.right);
    }

    public static void main(String[] args) {
        // Tree based on ARANAS:
        //             A
        //           /   \\
        //          R     A
        //         / \\     \\
        //        N   A     S
        Node root = new Node('A');
        root.left = new Node('R');
        root.right = new Node('A');
        root.left.left = new Node('N');
        root.left.right = new Node('A');
        root.right.right = new Node('S');

        System.out.print("Binary Tree BFS: ");
        bfs(root);

        System.out.print("\nBinary Tree DFS (Preorder): ");
        dfsPreorder(root);

        System.out.println();
    }
}
