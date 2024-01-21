class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def array_to_complete_binary_tree(arr):
    if not arr:
        return None

    n = len(arr)
    root = TreeNode(arr[0])

    queue = [root]
    i = 1

    while i < n:
        current = queue.pop(0)

        left_value = arr[i] if i < n else None
        right_value = arr[i + 1] if i + 1 < n else None

        if left_value is not None:
            current.left = TreeNode(left_value)
            queue.append(current.left)

        if right_value is not None:
            current.right = TreeNode(right_value)
            queue.append(current.right)

        i += 2

    return root

def print_level_order(root):
    if not root:
        return

    queue = [root]

    while queue:
        current = queue.pop(0)
        print(current.key, end=" ")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

# Example usage
input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
complete_binary_tree_root = array_to_complete_binary_tree(input_array)

print("Level-order traversal of the generated complete binary tree:")
print_level_order(complete_binary_tree_root)
