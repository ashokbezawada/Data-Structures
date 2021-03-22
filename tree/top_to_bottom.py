# The main goal of this code is to find the height of the tree using top down appraoch
# The function takes argument as root

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def find_height_recursion(root):
    if root is None:
        return -1
    lheight = find_height_recursion(root.left)
    rheight = find_height_recursion(root.right)
    return max(lheight,rheight) + 1


# Finding height of a tree iteratively

def find_height_iteratively(root):
    pass

# main
root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)

print(find_height_recursion(root))
