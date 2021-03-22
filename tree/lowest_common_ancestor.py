class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# The main goal of this function is to find the parents of every node and store them in parents dictionary
def find_parents(root,parent):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        if node.right is not None:
            parent[node.right.data] = node.data
            stack.append(node.right)
        if node.left is not None:
            parent[node.left.data] = node.data
            stack.append(node.left)
    return parent

# The main goal of this function is to find the lowest common ancestor
def lowest_common_ancestor(root,node1,node2):
    if root is None:
        return
    parent = {root.data:0}
    parent = find_parents(root,parent)
    path = set()
    path.add(node1)
    while node1 != 0:
        node1 = parent[node1]
        path.add(node1)
    while node2 not in path:
        node2 = parent[node2]
    print(node2)
    return node2

root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)
root.right.right.right = Node(8)
lowest_common_ancestor(root,8,5)

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.right = Node(4)
# root.right.left = Node(5)
# root.right.right = Node(6)
# root.right.left.left = Node(7)
# root.right.right.right = Node(8)
# lowest_common_ancestor(root,2,5)