# The main goal of this code is to print tree traversal in recursive way
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# The main goal of this function is to traverse the tree using inorder traversal 
# The function takes argument as root
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

# The main goal of this function is to traverse the tree using preorder traversal
# The function takes argument as root
def preorder(root):
    if root is not None:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

# The main goal of this function is to traverse the tree using post order traversal
# The function takes argument as root
def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)

# main
root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)

#inorder(root)
# preorder(root)
postorder(root)

