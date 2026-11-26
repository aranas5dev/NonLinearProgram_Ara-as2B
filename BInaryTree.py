
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Breadth-First Search (BFS)
# Visit nodes level by level.
def bfs(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        current = queue.popleft()
        print(current.data, end=" ")

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)


# Depth-First Search (DFS - Preorder)
# Visit Root, Left, Right.
def dfs_preorder(node):
    if node is None:
        return

    print(node.data, end=" ")
    dfs_preorder(node.left)
    dfs_preorder(node.right)


# Main Program
if __name__ == "__main__":

    root = Node('R')
    root.left = Node('A')
    root.right = Node('Y')

    root.left.left = Node('V')
    root.left.right = Node('E')

    root.right.left = Node('N')

    # Display BFS
    print("Binary Tree BFS: ", end="")
    bfs(root)

    # Display DFS
    print("\nBinary Tree DFS (Preorder): ", end="")
    dfs_preorder(root)

    print()
