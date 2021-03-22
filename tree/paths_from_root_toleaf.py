# The main goal of this function is to print all the paths from root to leaf
# The function takes argument root and stack

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def print_paths_from_root_toleaf(current,path):
    if current is None:
        return
    path.append(current.data)
    if current.left is None and current.right is None:
        print(path)
    print_paths_from_root_toleaf(current.left,path)
    print_paths_from_root_toleaf(current.right,path)
    path.pop()

# root = Node(1) 
# root.left = Node(2) 
# root.right = Node(3) 
# root.left.left = Node(4) 
# root.left.right = Node(5) 

root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)


print_paths_from_root_toleaf(root,[])
    