# Binary tree means a node can only have at most 2 sub trees

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)

        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, root, result):
        if root:
            self._inorder_traversal(root.left, result)
            result.append(root.key)
            self._inorder_traversal(root.right, result)


# Example usage:
bst = BST()
keys_to_insert = [8, 3, 10, 1, 6, 9, 12]

for key in keys_to_insert:
    bst.insert(key)

# Inorder traversal should give sorted order
print("Inorder Traversal:", bst.inorder_traversal())

# Search for a key
search_key = 6
search_result = bst.search(search_key)

if search_result:
    print(f"{search_key} found in the BST.")
else:
    print(f"{search_key} not found in the BST.")
