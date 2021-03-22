class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# The main goal of this function is to build a balanced binary search tree using a sorted array
def buildbalancedBst(sorted_array):
    if len(sorted_array) == 0:
        return None
    mid = len(sorted_array)//2
    root = Node(sorted_array[mid])
    root.left = buildbalancedBst(sorted_array[:mid])
    root.right = buildbalancedBst(sorted_array[mid+1:])
    return root

# The main goal of this function is to traverse in above created bst using inorder
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

# main 
arr = [1,2,3,4,5,6,7]
root = buildbalancedBst(arr)
inorder(root)
    