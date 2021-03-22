import sys
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# The main goal of this function is to check whether the given tree is bst or not
# This can be solved using inorder
def isBinarysearchtree(root):
    if root is None:
        return
    stack = []
    curr = root
    prev = None
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            if (prev and curr.data <= prev):
                return False
            prev = curr.data
            curr = curr.right
    return True

# main 
root = Node(1)
root.left = Node(2)
root.right = Node(15)
root.left.left = Node(1)
root.left.right = Node(4)
print(isBinarysearchtree(root))