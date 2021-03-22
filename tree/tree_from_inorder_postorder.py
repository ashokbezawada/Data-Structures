# The main goal of this function is to generate tree from inorder and postorder
# inorder = left ---> root ---> right
# post = left ----> right ----> root

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def generate_tree(postorder,inorder):
    if inorder:
        root = Node(postorder.pop())
        root_index = inorder.index(root.data)
        root.right = generate_tree(postorder,inorder[root_index+1:])
        root.left = generate_tree(postorder,inorder[:root_index])
        return root

# The main goal of this function is print the tree generated from above function in postorder and compare with
# Initital given postorder
def print_tree(root):
    if root is not None:
        print_tree(root.left)
        print_tree(root.right)
        print(root.data)

# main
root = generate_tree([9,15,7,20,3],[9,3,15,20,7])
print_tree(root)