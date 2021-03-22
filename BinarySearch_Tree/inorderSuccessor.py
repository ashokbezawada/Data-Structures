class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# The main goal of this function is to find the inorder successor in binary search tree
def inorderSuccessor(root,x):
    # pass
    while True:
        if x > root.data:
            root = root.right
        elif x < root.data:
            succ = root
            root = root.left
        else:
            if root.right:
                succ = findMin(root.right)
            break
        if root is None:
            return None
    return succ
    
# The main goal of this function is to find the min in right subtree
def findMin(current):
    while current.left is not None:
        current = current.left
    return current

root = Node(15)
root.left = Node(10)
root.left.left = Node(8)
root.left.right = Node(12)
root.left.left.left = Node(6)
root.left.right.left = Node(11)
root.right = Node(20)
root.right.left = Node(17)
root.right.right = Node(25)
result = inorderSuccessor(root,15)
print(result.data)

        