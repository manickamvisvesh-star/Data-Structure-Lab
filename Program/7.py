class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert_left(self, current_node, key):
        if current_node.left is None:
            current_node.left = Node(key)
        else:
            new_node = Node(key)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, key):
        if current_node.right is None:
            current_node.right = Node(key)
        else:
            new_node = Node(key)
            new_node.right = current_node.right
            current_node.right = new_node

    # Inorder Traversal
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    # Preorder Traversal
    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder Traversal
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")


# Main Program
if __name__ == "__main__":
    # Create tree with root
    tree = BinaryTree('10')

    # Insert nodes (same as manual diagram)
    tree.insert_left(tree.root, '11')
    tree.insert_right(tree.root, '12')
    tree.insert_left(tree.root.left, '13')
    tree.insert_right(tree.root.left, '14')
    tree.insert_left(tree.root.right, '15')

    print("Inorder Traversal:")
    tree.inorder(tree.root)

    print("\nPreorder Traversal:")
    tree.preorder(tree.root)

    print("\nPostorder Traversal:")
    tree.postorder(tree.root)
