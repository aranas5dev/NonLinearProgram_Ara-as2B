# Create Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# PREORDER: Root -> Left -> Right
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# INORDER: Left -> Root -> Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# POSTORDER: Left -> Right -> Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# ======================================
#         CREATE BINARY TREE
# ======================================

root = Node("R")

root.left = Node("A")
root.right = Node("Y")

root.left.left = Node("V")
root.left.right = Node("E")

root.right.left = Node("N")


# ======================================
#           DISPLAY RESULTS
# ======================================

print("================================")
print("    DFS METHODS IN TREE")
print("             RAYVEN")
print("================================")

print("\nPREORDER:")
preorder(root)

print("\n\nINORDER:")
inorder(root)

print("\n\nPOSTORDER:")
postorder(root)

print("\n\n================================")
print("          PROGRAM ENDED")
print("================================")
