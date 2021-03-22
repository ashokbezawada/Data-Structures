class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# The main goal of this is function is to insert a node in binary search tree
def insert(root,key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left,key)
    if key > root.data:
        root.right = insert(root.right,key)
    return root

# The main goal of this function is to find minimum in right sub tree
def findMin(root):
    # keep going to left until we reach end
    current = root
    while current.left is not None:
        current = current.left
    return current

# The main goal of this function is to delete a node from the binary search tree
def delete(root,key):
    if root is None:
        return root
    elif key < root.data:
        root.left = delete(root.left,key)
    elif key > root.data:
        root.right = delete(root.right,key)
    else:
        # leaf node
        if not root.left and not root.right:
            root = None
        # Node with one children
        elif not root.left:
            root = root.right
        elif not root.right:
            root = root.left
        else:
            temp = findMin(root.right)
            root.data = temp.data
            root.right = delete(root.right,temp.data)
    return root

# The main goal of this code is to traverse the tree using inorder
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

# Main 
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
delete(root,70)
inorder(root)

