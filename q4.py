class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        current = queue.pop(0)
        result.append(current.key)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)

result = level_order_traversal(root)
print("Level-order traversal:", result)
