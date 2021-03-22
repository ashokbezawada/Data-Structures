class Treenode:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

# The main goal of this function is to print the generated tree using inorder
# The function takes argument as root
def print_tree(root):
    if root is None:
        return
    print_tree(root.left)
    print(root.val)
    print_tree(root.right)

class solution(object):
    # The main goal of this function build a tree using inorder and postorder
    # The function takes argument as inorder and postorder
    def buildtree(self,inorder,postorder):
        #base condition
        if inorder:
            root = Treenode(postorder.pop())
            root_index = inorder.index(root.val)
            root.right = self.buildtree(inorder[root_index+1:],postorder)
            root.left = self.buildtree(inorder[:root_index],postorder)
            return root   
x = solution()
print_tree(x.buildtree([2,1,4,3,5],[2,4,5,3,1]))