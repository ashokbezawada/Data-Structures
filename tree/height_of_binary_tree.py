# The main goal of this function is to find the height of the binary tree
# The function takes arguments as root 

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def find_height(root):
    if root is None:
        return
    queue = [root]
    height = 0
    while True:
        node_count = len(queue)
        if node_count == 0:
            return height
        height += 1

        while node_count > 0:
            node = queue.pop(0)
            #queue.append(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            node_count -= 1

root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)

# root = Node(1) 
# root.left = Node(2) 
# root.right = Node(3) 
# root.left.left = Node(4) 
# root.left.right = Node(5) 

print(find_height(root))
