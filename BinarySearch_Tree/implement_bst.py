# The main goal of this code is to perform basic binary search tree operations
# which are search,insert and delete

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# The main goal of this function is to insert elements in binary search tree
def insert(root,key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left,key)
    elif key > root.data:
        root.right = insert(root.right,key)
    return root

# The main goal of this function is to print the tree in inorder fashion
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

# The main goal of this function is to search whether a key exists in binary tree or not
def search(root,key):
    if key == root.data:
        return True
    if key < root.data:
        if root.left != None:
            return search(root.left,key)
        return False
    if key > root.data:
        if root.right != None:
            return search(root.right,key)
        return False 



# Main 
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
inorder(root)
#print(search(root,50))
arr = [50,30,20,40,70,60,80,110,120]
for i in arr:
    print(search(root,i))





    