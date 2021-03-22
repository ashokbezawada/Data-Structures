# The main goal of this code is to print the level order traversal of the binary tree
# The function takes argument as root

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def level_order(root):
    if root is None:
        return
    # creating a queue to perform level order traversal
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)

level_order(root)
