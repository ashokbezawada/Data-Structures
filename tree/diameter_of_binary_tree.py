# The main goal of this code is to find the diameter of a binary tree
# The function takes argument as root 

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def find_diameter(root,diameter):
    if root is None:
        return 0,diameter
    lheight,diameter = find_diameter(root.left,diameter)
    rheight,diameter = find_diameter(root.right,diameter)
    # calculate diameter passing through that node is 
    max_diameter = lheight + rheight + 1
    # update the diameter 
    diameter = max(diameter,max_diameter)

    return max(lheight,rheight) + 1, diameter

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print(find_diameter(root,0)[1])
