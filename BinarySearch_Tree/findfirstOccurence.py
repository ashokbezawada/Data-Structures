class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# The main goal of this function is to find the first occurence of key
def findfirstOccurence(root,x):
    result = None
    while root!= None:
        if x < root.data:
            root = root.left
        elif x > root.data:
            root = root.right
        else:
            result = root.data
            root = root.left
    return result

# main
root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(7)
firstoccurence = findfirstOccurence(root,4)
print(firstoccurence)
