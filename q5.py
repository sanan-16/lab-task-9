class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def construct_expression_tree(postfix_expression):
    stack = []

    operators = set(['+', '-', '*', '/'])

    for symbol in postfix_expression:
        if symbol not in operators:
            # Operand: Create a leaf node and push it onto the stack
            node = TreeNode(symbol)
            stack.append(node)
        else:
            # Operator: Pop two operands from the stack and create a new internal node
            right_operand = stack.pop()
            left_operand = stack.pop()

            operator_node = TreeNode(symbol)
            operator_node.left = left_operand
            operator_node.right = right_operand

            # Push the new internal node onto the stack
            stack.append(operator_node)

    # The final item on the stack is the root of the expression tree
    return stack.pop()

def print_infix_expression(tree):
    if tree:
        if tree.left or tree.right:
            print("(", end=" ")
        print_infix_expression(tree.left)
        print(tree.value, end=" ")
        print_infix_expression(tree.right)
        if tree.left or tree.right:
            print(")", end=" ")

# Example usage
postfix_expression = "34+2*6-"
expression_tree_root = construct_expression_tree(postfix_expression)

print("Infix expression from the constructed expression tree:")
print_infix_expression(expression_tree_root)
