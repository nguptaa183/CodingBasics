class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")


def preOrder(node):
    if node:
        print(node.value, end=" ")
        preOrder(node.left)
        preOrder(node.right)


def inOrder(node):
    if node:
        inOrder(node.left)
        print(node.value, end=" ")
        inOrder(node.right)


def postOrder(node):
    if node:
        postOrder(node.left)
        postOrder(node.right)
        print(node.value, end=" ")


print("preOrder traversal")
preOrder(root)
print()

print("inOrder traversal")
inOrder(root)
print()

print("postOrder traversal")
postOrder(root)
print()
