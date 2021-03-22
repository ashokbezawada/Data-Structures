# The main goal of this code is to implement the tree traversals iteratively
# The function takes arguments as root

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

# Inorder left ---> root.data ---> right
def inorder_iterative(root):
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.data)
            curr = curr.right

# Preorder current ---> left --> right
def preorder_iterative(root):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.data)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

# Post order left ---> right ----> current
def post_order_iterative(root):
    if root is None:
        return
    first_stack = [root]
    second_stack = []
    while first_stack:
        node = first_stack.pop()
        second_stack.append(node.data)
        if node.left is not None:
            first_stack.append(node.left)
        if node.right is not None:
            first_stack.append(node.right)
    while second_stack:
        post_node = second_stack.pop()
        print(post_node)

#main
root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)

#inorder_iterative(root)
#preorder_iterative(root)
post_order_iterative(root)

