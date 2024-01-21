class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2

    # Middle element becomes the root of the BST
    root = TreeNode(nums[mid])

    # Recursively construct the left and right subtrees
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])

    return root

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.key, end=" ")
        print_inorder(root.right)

# Example usage
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bst_root = sorted_array_to_bst(sorted_array)

print("In-order traversal of the generated BST:")
print_inorder(bst_root)
