# The main goal of this code is to generate a binary tree from preorder and inorder traversal
# Preorder = root --->left --->right
# Inorder = left ---> root ----> right

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def generate_tree(preorder,inorder):
    if inorder:
        root = Node(preorder.pop(0))
        root_index = inorder.index(root.data)
        root.left = generate_tree(preorder,inorder[:root_index])
        root.right = generate_tree(preorder,inorder[root_index + 1 :])
        return root

# The main goal of this function is to print the tree generated from above function in preorder way
def print_tree(root):
    if root is not None:
        print(root.data)
        print_tree(root.left)
        print_tree(root.right)


# main
root = generate_tree([3,9,20,15,7], [9,3,15,20,7])
print_tree(root)

