# The main goal is to insert in binary search tree and search an element in binary search tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# Insert
def insert(root,key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left =  insert(root.left,key)
    if key > root.data:
        root.right = insert(root.right,key)
    return root

# Search
def search(root,key):
    if root.data == key:
        return True
    if key < root.data:
        if root.left is not None:
            return search(root.left,key)
        return False
    if key > root.data:
        if root.right is not None:
            return search(root.right,key)
        return False

# Inorder left --> current --> right
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

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



