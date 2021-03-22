# The main goal of this function is to check whether the tree is balanced or not
# The function takes argument as root and boolean value isbalanced

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def check_balance(root,isbalance = True):
    if root is None or not isbalance:
        return 0, isbalance
    lheight,isbalance = check_balance(root.left,isbalance)
    rheight,isbalance = check_balance(root.right,isbalance)
    if abs(lheight-rheight) > 1:
        isbalance = False
    return max(lheight,rheight) + 1, isbalance

root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.left.left.left = Node(10)
root.right = Node(6)
# root.right.left = Node(5)
# root.right.right = Node(7)

print(check_balance(root)[1])