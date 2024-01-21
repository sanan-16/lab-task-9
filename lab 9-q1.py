class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_bst(root):
    def in_order_traversal(node, values):
        if node:
            in_order_traversal(node.left, values)
            values.append(node.key)
            in_order_traversal(node.right, values)

    values = []
    in_order_traversal(root, values)

    # Check if the values are in sorted order
    for i in range(1, len(values)):
        if values[i] <= values[i - 1]:
            return False

    return True

# Example usage
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

result = is_bst(root)
print("Is the tree a BST?", result)
