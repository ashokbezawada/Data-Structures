class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# The main goal of this code is to find the lowest common ancestor in binary search tree
def lowestcommonAncestor(root,x,y):
    while root:
        if(x < root.data and y < root.data):
            root = root.left
        if (x > root.data and y > root.data):
            root = root.right
        else:
            return root

# main
root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14) 

result = lowestcommonAncestor(root,10,22)
print(result.data)
        
