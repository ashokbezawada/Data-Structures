class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# The main goal of this function is to find the find the elements in the given range
def rangeQuerying(root,low,high):
    if root is not None:
        if low < root.data:
            rangeQuerying(root.left,low,high)
        if low <= root.data and high >= root.data:
            print(root.data)
        if high > root.data:
            rangeQuerying(root.right,low,high)

root = Node(15)
root.left = Node(10)
root.left.left = Node(8)
root.left.right = Node(12)
root.left.left.left = Node(6)
root.left.right.left = Node(11)
root.right = Node(20)
root.right.left = Node(17)
root.right.right = Node(25)

rangeQuerying(root,15,20)